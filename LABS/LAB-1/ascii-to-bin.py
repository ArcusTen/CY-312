#!/usr/bin/env python3
from pwn import log     # just for better printing output nothing else

with open('input.txt', 'r') as file:
    targetASCII = file.read().strip()

def DecimalToBinary(num):
    return bin(num)[2:]  # Convert number to binary string

def BinaryToDecimal(binary):
    return int(binary, 2)


binary_list = []
for i in targetASCII:
    targetBIN = DecimalToBinary(ord(i))
    binary_list.append(targetBIN)
    log.info(f"Binary of '{i}':- {targetBIN}")

print(" ")
log.info("CHARACTERS FRO BIN:-")
for binary in binary_list:
    print(chr(BinaryToDecimal(binary)), end='')
print()
