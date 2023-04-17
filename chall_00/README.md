# Challenge 00 Write-Up
## Info
```
a.out: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=a1c1ed776f871bc968d8aa561e2f35de9338e1b3, for GNU/Linux 3.2.0, not stripped
```
```
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Full RELRO      No canary found   NX enabled    PIE enabled     No RPATH   No RUNPATH   67 Symbols        No    0               1               a.out
```

## Method
Buffer Overflow

## Details
Basic buffer overflow, just overwrite the value

Compiled with `gcc main.c -fno-stack-protector`. 
