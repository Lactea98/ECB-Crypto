#!/usr/bin/python3

from Crypto.Cipher import AES
import random

def padding(msg):
    return msg + chr(block_size - len(msg) % block_size) * (block_size - len(msg) % block_size)

def unpadding(msg):
    return msg[0:-ord(msg[-1])]

# Generate random SALT
def generate_SALT():
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars=[]
    
    for i in range(random.randint(10,14)):
        chars.append(random.choice(ALPHABET))
    return "".join(chars)
    
def decryption(crypto_text):
    cycle = int(len(msg) / block_size)
    cipherText = list()
    while cycle != 0:
        tmp = crypto_text[0:32]
        cipherText.append(decipher.decrypt(tmp.decode('utf-8')))
        crypto_text = crypto_text[32:]
        cycle -= 1
    print("".join(cipherText))


block_size = 16          # Block size
key = "Un1v3rs3_awesome" # AES key
# SALT = generate_SALT()    # Random SALT
SALT = "R@nd0mVaLu3"
msg = ''                 # User input value
flag = 'flag{flag_test_T35t}'   # flag

cipher = AES.new(key, AES.MODE_ECB)
decipher = AES.new(key, AES.MODE_ECB)


while True:
    msg = input("Input value: ")
    msg = padding(SALT + str(msg) + flag)
    crypto_text = cipher.encrypt(msg).hex()
    
    print(crypto_text)
        
    ## Decrypt
    # decryption(crypto_text)