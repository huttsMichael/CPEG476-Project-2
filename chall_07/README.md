# Challenge 07 Write-Up
## Info
```
chall_07: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=ce0f32b229bbd5e1b175dfe30dc8ea215e8ad8f1, for GNU/Linux 3.2.0, not stripped
```
```
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Full RELRO      Canary found      NX disabled   PIE enabled     No RPATH   No RUNPATH   68 Symbols        No    0               1               chall_07
```

## Method
Shellcode

## Details
Literally just drop the shellcraft payload into the input.