# Challenge 11 Write-Up
## Info
```
chall_11: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=e15d478b7aa103299f0d72ceb37f9c0dac550cea, for GNU/Linux 3.2.0, not stripped
```
```
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   Canary found      NX enabled    No PIE          No RPATH   No RUNPATH   75 Symbols        No    0               2               chall_11
```

## Method
printf

## Details
Easy once I familiarized myself with fmtstr_payload