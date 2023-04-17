# Challenge 02 Write-Up
## Info
```
withoutpie: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=76e18d44f9d59692abd52786472bcabf378dd507, for GNU/Linux 3.2.0, not stripped
```
```
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    No PIE          No RPATH   No RUNPATH   69 Symbols        No    0               1               withoutpie
```

## Method
Buffer Overflow

## Details
Overwrite the return address

Compiled with `gcc -m32 main.c -fno-stack-protector` 

Should have PIE turned off, PWN the "withoutpie" version
