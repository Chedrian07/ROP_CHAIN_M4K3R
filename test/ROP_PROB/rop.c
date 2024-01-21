#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>


//gcc -fno-stack-protector -no-pie rop.c -o rop
// [*] '/home/kch3dri4n/dev/ROP_CHAIN_M4K3R/test/ROP_PROB/rop'
//     Arch:     amd64-64-little
//     RELRO:    Partial RELRO
//     Stack:    No canary found
//     NX:       NX enabled
//     PIE:      No PIE (0x400000)

void rop_gadget(){
    __asm__("pop %rdi; ret");
    __asm__("pop %rsi; ret");
    __asm__("pop %rdx; ret");
    __asm__("pop %rcx; ret");
    __asm__("pop %r8; ret");
    __asm__("pop %r9; ret");
    __asm__("pop %rax; ret");
}

void vuln_bof(){
    char buf[100];

    printf("Go BOF : "); // Fix typo in printf function call
    read(0,buf,200);
}

int main(){
    vuln_bof();
}