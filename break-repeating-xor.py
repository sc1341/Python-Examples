#!/usr/bin/env python3

import base64, collections, string

human = ["the", "dog", "cat", "at", "then", "because"]

encrypted = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

def chunk(data, keysize):
    return [data[i:i+keysize] for i in range(0, len(data),keysize)]

def xor_decryptor(s: str, key: str) -> str:
    decrypted = ""
    for i in range(0, len(s), 2):
        decrypted += chr(int(s[i], 16) ^ ord(key))
    return decrypted

def ascii_to_bin(s : str):
    new = ""
    for i in s:
        convert = bin(ord(i))[2:]
        new +=   '0' * (8-len(convert)) + convert
        
    return new

def calculate_hamming_distance_ascii(a : str, b : str):
    if len(a) != len(b):
        raise Exception("Hamming error")
    
    a = ascii_to_bin(a)
    b = ascii_to_bin(b)
    d = 0
    for i in range(0, len(a)):
        if a[i] != b[i]:
            d += 1
    return d


def calculate_hamming_distance_bytes(a : bytes, b : bytes):
    d = 0
    for i in range(0, len(a)):
        if a[i] != b[i]:
            d += 1
    return d


def find_keylength(c : str):
    data = {}
    for keysize in range(1,10):
        data[keysize] = calculate_hamming_distance_bytes(c[0:keysize], c[keysize:keysize*2])/keysize
    smallest = 10
    value = 0
    for i in data:
        if smallest > data[i]:
            smallest = data[i] 
            value = i

    print(f"Smallest average hamming distance indicates the following keylength: {value}")
    return value
    

def single_byte_xor(data :str, key : str):
    return chr(data ^ ord(key))


def transpose_blocks(blocks):
    """
    ['abc', 'abc', 'abc'] -> ['aaa', 'bbb', 'ccc]
    """
    transposed_tuples = list(zip(*blocks))
    return [list(sublist) for sublist in transposed_tuples]

def english_score(data):
    """
    Returns True if is a possible candidate, or False if not
    :bool:

    This could be improved with letter frequency ditribution or space analysis. 
    """
    common_words = ["the", "is", "and", "because", "if", "of"]
    data = data.lower()
    if data.lower().split(' ').count(' ') > 3:
        return True 

    for word in common_words: 
        if word in data:
            return True 
        else:
            pass
    
    return False

def derive_key(blocks, keysize, key):
    """
    The key can be derived by determing the most common hex value for a given character on each block
    """
 
    transposed = transpose_blocks(blocks)
    new = []
    nb = []
    for block in transposed:
        clear = ""
        for i in block:
            clear += single_byte_xor(i, key)
        nb.append(clear)
    
    print(nb)
        


t1 = "this is a test"
t2 = "wokka wokka!!!"

# Verify that the implementation of the ascii hamming distance is correct according to the example
assert calculate_hamming_distance_ascii(t1,t2) == 37

data = ""
for line in open("encrypted.txt", "r"):
    data += line.strip('\n')

xor_data = base64.b64decode(data.encode())
print(xor_data)

keysize = find_keylength(xor_data)
chunks = chunk(xor_data, keysize)
print(f"Keysize (guess): {keysize}")

for i in string.ascii_letters:
    derive_key(chunks, keysize, i)