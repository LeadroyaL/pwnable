### mistake

这题一下真没看出来，hint是运算符优先级
问题出在`fd = open('/home/mistake/password',O_RDONLY,0400)<0)`，文件不存在返回0，小于号优先，故fd=(0<0)=0

即fd代表标准输入，我们的读到了pw_buf里；之后用scanf将第二次输入的内容读到了pw_buf2里；所以程序完全可控

exp
```
./mistake (waiting) 0000000000<br> 1111111111<br>
```

flag
`Mommy, the operator priority always confuses me :(`
