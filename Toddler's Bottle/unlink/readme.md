### unlink

这题模拟的堆溢出的题型，比实际中的少了很多保护，利用起来比较简单。

思路：堆溢出造成的 **有一定限制的任意地址写** ，具体写哪里，然后这个题有info leak，可以搞一下。

---

每个结构体是0x10大小，看一下堆结构

0x804b410:	0x0804b428(fd)	0x00000000  0x3636363636363636(input)  0x00000000	0x00000019
0x804b428:  0x0804b440(fd)	0x0804b410(bk)  0x00000000  0x00000000	0x00000000	0x00000019
0x804b428:  0xaaaaaaaa(fd)	0xbbbbbbbb(bk)  0x00000000  0x00000000	0x00000000	0x00000019
0x804b440:	0x00000000	0x0804b428(bk)	0x00000000	0x00000000  0x00000000	0x00000409

```
void unlink(OBJ* B){
	OBJ* BK;
	OBJ* FD;
	BK=B->bk;  BK = 0xbbbbbbbb
	FD=B->fd;  FD = 0xaaaaaaaa
	FD->bk=BK;  [0xaaaaaaaa+8] 写为 0xbbbbbbbb
	BK->fd=FD;  [0xbbbbbbbb] 写为 0xaaaaaaaa
}
```

---

这时候我有一个错误的思路，将栈地址上的main-ret写掉，有如下的exp

`print '6'*4*4 +'\xbc\xbc\xa1\xbf'+'\xeb\x84\x04\x08'`

将`addr(A)+0x28`写为`0x080484EB`

即0xaaaaaaaa = 0x0804866C; 0xbbbbbbbb = 0x080484EB;

然后发现不可以这么做，因为堆的地址每次都会变，gdb关掉了这个功能，所以需要重新弄一下

----

后来又想到一个问题，unlink是有两次写数据的，要让程序不崩掉，需要保证两处都是可以写的，上面我们的思路造成了两处写

```
stack[ret] = addr(get_shell)
addr(get_shell) = addr(stack[ret])
（省略offset）
```

get_shell在text段，显然不可以写入数据，此思路gg


只能写`fini_array`

使用这个命令`readelf -S unlink`
`[19] .fini_array       FINI_ARRAY      08049f0c 000f0c 000004 00  WA  0   0  4`

表示程序执行完了以后，跳到0x8048f0c

但还是之前的问题 addr(FINI_ARRAY) 与 addr(get_shell)的地址会相互写入对方的附近，显然text段是不可以写的

-----

**有写权限的段在IDA里ctrl+s是可以看的**

![pic0](pic0.png)

看来这题只能写栈和写堆，进行栈迁移，再使用ROP进行get_shell。

堆地址和栈地址均随机，好在这个题提供了这两个的位置。
