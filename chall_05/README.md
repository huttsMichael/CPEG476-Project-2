# Challenge 05 Write-Up
## Info
```
chall_05: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=429a18a195d1ca2ea2ec1c8bd229ed582dcf6027, for GNU/Linux 3.2.0, not stripped
```
```
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Full RELRO      No canary found   NX enabled    PIE enabled     No RPATH   No RUNPATH   70 Symbols        No    0               2               chall_05
```

## Method
Buffer Overflow with Leak

## Details
A bit more complex to find everything, concepts themselves not too advanced.