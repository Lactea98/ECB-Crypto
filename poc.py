#!/usr/bin/python

import string
from pwn import *
import time

p = remote("localhost", 7202)
send_data = 'a'
front = ''
length = ''

print ("Guessing..")
while True:
    p.recvuntil("Input value: ")    
    p.sendline(send_data)
    result = p.recvline()
    print(result)
    print(send_data)
    
    if front == result[:32]:
        length = len(send_data)
        break
    else:
        front = result[:32]
        send_data += 'a'
    
    
print ("Finding flag...")
count = 14 + len(send_data)
flag = ''
 
while count != 0:
    p.recvuntil("Input value: ")
    p.sendline("a"*count)
    result = p.recvline()
    result = result[32:64]
    # print("Result: " + result)

    for char in string.printable:
        send_data2 = "a"*count + flag + char
        p.recvuntil("Input value: ")
        p.sendline(send_data2)
        
        result2 = p.recvline()
        result2 = result2[32:64]
        
        print(send_data2)
        print(result + " " + result2)
        
        if result == result2:
            count -= 1
            flag += char
            print(">>> " + flag)
            
            break
        print("")
        # time.sleep(0.2)
            
            
print(result)