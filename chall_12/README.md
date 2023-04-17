# Challenge 12 Write-Up
## Info
```
chall_12: ELF 32-bit LSB pie executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=54c96c24cf3f6258c22dea4a5cf8da1a9ec127db, for GNU/Linux 3.2.0, not stripped
```
```
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
No RELRO        Canary found      NX enabled    PIE enabled     No RPATH   No RUNPATH   78 Symbols        No    0               2               chall_12
```

## Method
printf + leak

## Details
fmtstr_payload but with a leak this time