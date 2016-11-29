### bof

nc pwnable.kr 9000

`gets(char* buf)` 接收到EOF或者0x0A(\n)就停下，没有长度限制造成的溢出

由于buf在栈上，参数也在栈上，造成的数据覆盖；
虽然开启了canary保护，但在return之前就已经被getshell，所以不重要。

pwntools中`pack()`会按照默认LSB的方式去将`0x12345678`变为 `str(\x78\x56\x34\x12)`的格式

flag
```
daddy, I just pwned a buFFer :)
```
