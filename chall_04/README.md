# Challenge 04 Write-Up
## Info
```
chall_04: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=6a88b76aa9eaaa7d5d9d3d9e8fe23506f2bb9379, for GNU/Linux 3.2.0, not stripped
```
```
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    No PIE          No RPATH   No RUNPATH   67 Symbols        No    0               1               chall_04
```

## Method
Buffer Overflow

## Details
Another simple buffler overflow, that turned into a bit of a headache to get the offset right.