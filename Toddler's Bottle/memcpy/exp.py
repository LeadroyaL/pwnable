from pwn import *

context.log_level = 'debug'
r = remote('pwnable.kr',9022)

r.recvuntil(':')
r.recvuntil(':')

# 8-16
r.recvuntil(': ')
r.sendline('8')

# 16-32
r.recvuntil(': ')
r.sendline('16')

# 32-64
r.recvuntil(': ')
r.sendline('32')

# 64-128
r.recvuntil(': ')
r.sendline('64')

# 128-256
r.recvuntil(': ')
r.sendline('128')

# 256-512
r.recvuntil(': ')
r.sendline('256')

# 512-1024
r.recvuntil(': ')
r.sendline('512')

# 1024-2048
r.recvuntil(': ')
r.sendline('1024')

# 2048-4096
r.recvuntil(': ')
r.sendline('2048')

# 4096-8192
r.recvuntil(': ')
r.sendline('4096')

while True:
    r.recvline()
