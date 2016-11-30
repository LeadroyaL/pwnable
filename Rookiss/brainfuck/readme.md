### brainfuck

nc pwnable.kr 9001

**主要技巧：改写got表来控制EIP跳转，改写got表来实现函数调用的替换。**

brainfuck的模型，首先看到`tape`的位置，在bss段，上面翻一点是data段，很短，在向上就是got/plt表，所以思路就很明确了。

通过移动tape的方式来info leak，拿到libc里函数的地址。

`+`和`-`只影响写数据，`<`和`>`只影响指针移动，所以要先实现任意写，再去实现getshell。

循环里涉及到2个函数，`putchar`和`getchar`和`puts`，显然`puts`可以作为一个布置好以后进行跳转的入口。

我们要实现system("/bin/sh")得有这个string，第一反应是在libc里去找，但感觉ROP起来太麻烦了，而且栈也不好布置；然后就想到了怎么去输入，看到一个嵌套的结构，

1. 移动到那个got段
2. 读出一个函数的地址，算出system、gets的地址
3. memset改为gets，fgets改为system就可以实现输入"/bin/sh"
4. getshell

下面是[cmc_SARS](https://github.com/dmxcsnsbh)提供的思路
got表中的`strlen`可以被改为`system`，而且strlen的参数是我们输入的string，可以造成system("/bin/sh")

详细步骤：(感觉可以尝试输入"/bin/sh " + "brainfuck_code")
1. 移动到got段
2. 读出一个函数的地址，算出system的地址
3. 改写strlen的地址，改为system
4. 改写puts的地址，跳转到那个运行strlen的前面，这里选择跳到fgets前面，
5. 获得输入"/bin/sh"的机会
6. getshell!!!


flag:
``
