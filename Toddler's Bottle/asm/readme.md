### asm

规则：
1. 只允许open,read,write,exit这些syscall，其他都不允许
2. 给了一个mmap，固定地址，用来存放我们的东西
3. 删了'/'这个根目录，意思是只能用syscall
4. 清空了所有寄存器，尽情写shellcode吧！
5. shellcode不要超过0x1000长

思路：将下文的C翻译成机器码即可

```c
char *fileName = "";
int fd = open(fileName, FLAG);  //<---一般来说这个fd是3
read(fd,buf,1024);
write(1,buf,1024);
```

无法运行`./asm: error while loading shared libraries: libseccomp.so.2: cannot open shared object file: No such file or directory`

依赖`apt-get install libseccomp-dev`

有个神奇的指令叫`syscall`

64位参考链接http://blog.rchapman.org/posts/Linux_System_Call_Table_for_x86_64/

进行syscall的时候，`rax`表示编号，`%rdi	%rsi	%rdx	%r10	%r8	%r9`表示6个参数
rax  | syscall   
--|--
0 | read
1 | write
2 | open


将那段C改写一下（**注意，此处的syscall函数并不是syscall指令，而是被libc包转过的syscall**）

```c
int fd = syscall(2,fileName, FLAG); //<---一般来说这个fd是3
syscall(0,fd,buf,1024);
syscall(1,1,buf,1024);
```

这两段C经过测试都是可以正常运行的。

所以我们需要花时间写汇编，然后转成机器码、丢上去，而且是位置无关代码。

主要思路：
1. 文件名是很长的，需要用汇编手动一个一个输入，期间夹杂的技巧也就是一些循环，jmp之类的，需要把个数严格控制好（**很容易出错的地方**）
2. 调用3次syscall，分别是open,read,write
3. 后面崩了就崩了，别管就行


主要坑点：
1. AT&T指令和Intel指令的mov、cmp啥的都是不一样的
2. 汇编有些指令的语法不容易写对
3. 大小端不分
4. `syscall`汇编指令，和`syscall()`函数是两个不同的概念！不要混淆！
5. sys_open的参数要给全。。。
6. 这题坑了我N个小时。。。报警了

基本看一遍poc就懂了  `gcc -z execstack poc.c`

最后ssh上去，在tmp下创建一个文件写入shellcode，用`nc 0 9026 < /tmp/xxx`即可

flag
`Mak1ng_shelLcodE_i5_veRy_eaSy`
