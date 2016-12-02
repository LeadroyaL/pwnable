from pwn import *

context.log_level = 'debug'
r = remote('pwnable.kr',9022)

r.recvuntil(':')
r.recvuntil(':')

# 8-16
r.recvuntil(': ')
r.sendline('13')

# 16-32
r.recvuntil(': ')
r.sendline('20')

# 32-64
r.recvuntil(': ')
r.sendline('56')

# 64-128
r.recvuntil(': ')
r.sendline('120')

# 128-256
r.recvuntil(': ')
r.sendline('184')

# 256-512
r.recvuntil(': ')
r.sendline('504')

# 512-1024
r.recvuntil(': ')
r.sendline('1016')

# 1024-2048
r.recvuntil(': ')
r.sendline('2040')

# 2048-4096
r.recvuntil(': ')
r.sendline('4088')

# 4096-8192
r.recvuntil(': ')
r.sendline('4096')

flag = r.recvline_startswith('flag')
print flag
