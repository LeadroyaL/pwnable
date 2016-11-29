### leg

考察arm汇编

1. arm的PC保存的是下 **两条** 指令的地址，因为CPU的流水线结构是三级的，key1 = 0x00008cdc+ 8 = 0x8ce4
2. thumb的PC保存的是下 **一条** 指令的地址，而且后面显式+4， 故key2 = 0x00008d04 + 4 +4 = 0x00008d0C
3. `lr`指令表示返回地址，key3 = 0x00008d80

sum = 0x1a770(108400)


flag:
`My daddy has a lot of ARMv5te muscle!`
