### asm

规则：
1. 只允许open,read,write,exit这些syscall，其他都不允许
2. 给了一个mmap，固定地址，用来存放我们的东西
3. 删了'/'这个根目录，意思是只能用syscall
4. 清空了所有寄存器，尽情写shellcode吧！
