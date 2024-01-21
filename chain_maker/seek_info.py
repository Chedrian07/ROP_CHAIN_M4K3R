import os
import subprocess
import time
import sys
from pwn import *

file_path = os.path.abspath(sys.argv[1])
print(file_path)

def check_file():
    if os.path.exists(file_path):
        print("File exists")
        return True
    else:
        print("File not found")
        exit()
        
        
def analyze_elf():
    #Radare
    print("Analyzing ELF with Radare2")
    #radare2 -c 'aaa; s main; pdf~call' -q example.bin
    command = f"radare2 -e bin.relocs.apply=true -c 'aaaa; s main; pdf~call' -q {file_path} | grep -v -e 'sym.imp' -e 'reloc.'"
    os.system(command)

if __name__ == "__main__":
    check_file()
    analyze_elf()