import os
import subprocess
import time
import sys
from pwn import *
import subprocess

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
    print("*"*30 +" Analyzing ELF with Radare2 "+"*"*30)
    
    radare_command ="r2 -A -qc \"aaa; ss main; pdf\" " + file_path
    
    result = subprocess.run(radare_command, shell=True, capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    check_file()
    analyze_elf()