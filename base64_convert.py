#!/usr/bin/env python3


s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
answer = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

b64_value_lookup = {'000000': 'A', '000001': 'B', '000010': 'C', '000011': 'D', '000100': 'E', '000101': 'F', '000110': 'G', '000111': 'H', '001000': 'I', '001001': 'J', '001010': 'K', '001011': 'L', '001100': 'M', '001101': 'N', '001110': 'O', '001111': 'P', '010000': 'Q', '010001': 'R', '010010': 'S', '010011': 'T', '010100': 'U', '010101': 'V', '010110': 'W', '010111': 'X', '011000': 'Y', '011001': 'Z', '011010': 'a', '011011': 'b', '011100': 'c', '011101': 'd', '011110': 'e', '011111': 'f', '100000': 'g', '100001': 'h', '100010': 'i', '100011': 'j', '100100': 'k', '100101': 'l', '100110': 'm', '100111': 'n', '101000': 'o', '101001': 'p', '101010': 'q', '101011': 'r', '101100': 's', '101101': 't', '101110': 'u', '101111': 'v', '110000': 'w', '110001': 'x', '110010': 'y', '110011': 'z', '110100': '0', '110101': '1', '110110': '2', '110111': '3', '111000': '4', '111001': '5', '111010': '6', '111011': '7', '111100': '8', '111101': '9', '111110': '+', '111111': '/'}


def str_to_bin(s : str) -> str:
    new = ""
    for i in s:
        n = bin(ord(i))[2:]
        while len(n) < 8:
            n = '0' + n
        new += n
    return new
        

def hex_to_bin(h):
    new = ""
    for i in range(0,len(h),2):
        n =  str(bin(int(h[i:i+2], 16))[2:])
        n = (8-len(n)) * '0' + n # Pad to make a full  byte (8 bits)
        new += n
    return new


def str_to_base64(s : str):
    #b = str_to_bin(s)
    b = hex_to_bin(s)
    new = []
    for count in range(0, len(b), 6):
        try:
            new.append(b[count:count+6])
        except:
            new.append(b[count:])
    print(new)
    # Ensure that the last sextet contains the full 6 bits, otherwise the algorithm will fail programatically due to the
    # lookup table that we made earlier
    while len(new[-1]) < 6:
        new[-1] = new[-1] + '0'

    n = ""
    for value in new:
        n += b64_value_lookup[value]

    while (len(n) % 4) != 0:
        n += "="

    return n
        
value = str_to_base64(s)
if value == answer:
    print("WIN")
    print(f"{value} == {answer} -> TRUE")
    