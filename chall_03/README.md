# Challenge 03 Write-Up
## Info
```
chall_03: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=ea403916cf23cae02153abfc5de62994dcdb28b0, for GNU/Linux 3.2.0, not stripped
```
```
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Full RELRO      No canary found   NX disabled   PIE enabled     No RPATH   No RUNPATH   68 Symbols        No    0               2               chall_03
```

## Method
Leaked Address + Shellcode

## Details
First example using shellcode. Just overwrite the return address and pop a shell with pwn.shellcraft()
