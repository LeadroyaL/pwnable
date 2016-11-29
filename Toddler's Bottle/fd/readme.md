### fd

scp复制文件```scp -r -P2222 fd@pwnable.kr:~/fd* ./```

ignore目录格式 ```/**/bin/```

`int atoi(char * decimal)` in C likes `Integer.parseInt(String s)` in Java

`read(fd, char* buf , int size)`

0->stdin
1->stdout
2->stderr

将read的第一个参数指定为stdin即可

exp:

```
./fd 4660 <br>
LETMEWIN <br>```
