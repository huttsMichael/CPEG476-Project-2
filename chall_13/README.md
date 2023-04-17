# Challenge 13 Write-Up
## Info
```
chall_13: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=50d7f91524fb809e3d7c9fa548720f94bb821eaf, for GNU/Linux 3.2.0, not stripped
```
```
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    No PIE          No RPATH   No RUNPATH   71 Symbols        No    0               1               chall_13
```

## Method
Buffer Overflow

## Details
Another buffer overflow the win functions just called systemfunc this time