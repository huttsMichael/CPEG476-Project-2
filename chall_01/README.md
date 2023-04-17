# Challenge 01 Write-Up
## Info
```
a.out: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=1e2ba83e9de79887ac7819ca1fe4aa3ff49fa409, for GNU/Linux 3.2.0, not stripped
```
```
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Full RELRO      No canary found   NX enabled    PIE enabled     No RPATH   No RUNPATH   68 Symbols        No    0               1               a.out
```

## Method
Buffer Overflow

## Details
Basic buffer overflow, just overwriting two values this time.