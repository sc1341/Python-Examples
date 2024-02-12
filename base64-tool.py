#!/usr/bin/env python3

import sys

base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
padding = "="
base64_lookup = {}


def ascii_to_hex(s):
    return ''.join(hex(ord(value))[2:] for value in s)

def chunk(l: str, n: int):
    return [l[i:i+n] for i in range(0, len(l), n)]

# Generate the base64_lookup chart from base64 standard
for i, v in enumerate(base64_chars):
    b = bin(i)[2:]
    index = str((6-len(b)) * '0') + b
    # Example: '000000': 'A'
    base64_lookup[index] = v

def hex_char_to_8_bits(h):
    char =  str(bin(int(h, 16))[2:])
    return (8-len(char)) * '0' + char # Pad byte part to make a full  byte (8 bits)

def hex_to_base64(text):
    binary, base_64 = "", ""
    # Turn the hex chunks of 2 characters to 8 bits
    for value in chunk(text, 2):
        binary += hex_char_to_8_bits(value)
    binary = chunk(binary, 6)
    # Iterate through the binary string in chunks of 6 to map string to base64 encoded character
    for i in binary:
        try:
            base_64 += base64_lookup[i]
        except KeyError:
            i += '0' * (6-len(i))
            base_64 += base64_lookup[i]
    # Make sure the string is properly padded
    while (len(base_64) % 4) != 0:
        base_64 += padding
    print(f"Base64 encoded: {base_64}")
    return base_64


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 base64-tool.py [string]")
        sys.exit()
    return hex_to_base64(ascii_to_hex(sys.argv[1]))

if __name__ == "__main__":
    main()