### cmd1

1. 破坏了环境变量PATH
2. 过滤sh flag tmp

本来打算用python跑一段，发现tmp文件被过滤了；
于是准备python -c跑一段，发现引号解析起来会bug；
最后选择直接跑进python shell自由发挥；
于是`./cmd1 "/usr/bin/python"`直接进shell，import os随意发挥

flag
`mommy now I get what PATH environment is for :)`


另外几种解法：
1. `./cmd1 "/bin/cat /home/cmd1/f*"`
