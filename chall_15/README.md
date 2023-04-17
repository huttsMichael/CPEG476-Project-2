# Challenge 15 Write-Up
## Info
```
chall_15: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=132611036b789092b3e5c7acb2673007d7afd5b3, for GNU/Linux 3.2.0, not stripped
```
```
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Full RELRO      No canary found   NX disabled   PIE enabled     No RPATH   No RUNPATH   69 Symbols        No    0               2               chall_15
```

## Method
Shellcode + Leak

## Details
Classic shellcode situation but also overwriting some values to prevent exiting before I can escape