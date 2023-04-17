import pwn

pwn.context.arch = 'amd64'
elf = pwn.context.binary = pwn.ELF("./chall_09")


p = pwn.process(elf.path)
payload = elf.string(elf.sym.key)
p.sendline(pwn.xor(payload, 61))
p.interactive()


