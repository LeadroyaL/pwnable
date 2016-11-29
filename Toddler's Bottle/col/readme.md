### collision

输入char[20]转化为int[5]，之后求和并且与target对比，有以下几点注意：
1. LSB格式，即可0x12345678存储为\x78\x56\x34\x12
2. 使用argv[1]接受参数，不接受的有 \x00, 0x09, \x0A, \x20,

linux shell命令格式
```
 ./col `python -c "print '\x??\x??'"`
 ```

0x21DD09EC = 0x01010101 * 4 + 0x1DD905E8

exp
```
./col `python -c "print '\x01'*16+'\xE8\x05\xD9\x1D'"`
```

flag
```
daddy! I just managed to create a hash collision :)
```
