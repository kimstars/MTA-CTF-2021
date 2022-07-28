#!/usr/bin/env python
from Crypto.Util.number import *
import  gmpy2
import random
from flag import FLAG
import sys,os

def Encrypt(g,n,data):
    num = bytes_to_long(data)
    res = pow(g,num,n*n)
    r = random.randint(0,n-1)
    magic = pow(r,n,n*n)
    res = (res*magic)%(n*n)

    return long_to_bytes(res).hex()

def Decrypt(phi,n,u,data):
    num = bytes_to_long(data)
    res = pow(num,phi,n*n)
    res = (res - 1)//n
    res = (res*u)%n
    return long_to_bytes(res).hex()


if __name__ == '__main__':
    p = getPrime(512)
    q = getPrime(512)
    n = p*q
    phi = (p-1)*(q-1)
    g = n+1
    u = gmpy2.invert(phi,n)
    print("n=", n)
    print('Here is the flag:')
    print(Encrypt(g,n,FLAG.encode()))
    for i in range(10):
        try:
            m =str(input("Option:"))
            if m[0] == 'A':
                m = str(input("Message:"))
                try:
                    m = bytes.fromhex(m)
                    print(Encrypt(g,n,m))
                except Exception as e:
                    print(e)
                    print('Error')
                    exit(0)

            elif m[0] == 'B':
                m = str(input("Ciphertext:"))
                try:
                    m = bytes.fromhex(m)
                    message = Decrypt(phi,n,u,m)
                    message_text = (bytes.fromhex(message))
                    if message_text == FLAG.encode():
                        print("No no, I can't show flag!")
                    else: 
                        print(message)
                except Exception as e:
                    print(e)
                    print('Error')
                    exit(0)
        except Exception as e:
            print(e)
            print('Error')
            exit(0)