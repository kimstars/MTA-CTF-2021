#!/usr/bin/env python3

from Crypto.Cipher import AES
from MD21 import MD21
from os import urandom
from base64 import b64encode , b64decode
from flag import FLAG

my_secret = "********" # this is hidden
banner = '''1: generate cookie
2: get flag
3: exit
'''

def make_cookies():
    try:
        username = str(input("Username: "))
        string_cookies = "username="+username + "&isAdmin=false"

        h =  MD21((my_secret + string_cookies).encode()).hexdigest()
        print((b"Cookies: " + b64encode(string_cookies.encode())+b"." + h.encode()).decode("utf-8"))
    except :
        print("Error gen cookies")

def get_flag():
    try:
        cookies = str(input("Cookies: "))
        val, sig = cookies.split('.')
        string_cookies = b64decode(val.encode())
        
        hash = MD21((my_secret.encode() + string_cookies)).hexdigest()

        if hash != sig: 
            raise Exception("Signature error")
        val_dict = {}

        for i in b64decode(val).split(b'&'):
            b = i.split(b"=")
            val_dict[b[0]] = b[1]
        if val_dict[b'isAdmin'] == b'true':
            print(FLAG)
        else:
            print("Hello, ", val_dict[b'username'].decode('utf-8'))
    except Exception as e:
        print("Error: ", e)
if __name__ == "__main__":
    print(banner)
    for count in range(20):
        try:
            option = int(input("Option:"))
            if option == 1:
                make_cookies();
            elif option == 2:
                get_flag();
            elif option == 3:
                print("Bye!!!!!")
                break
            else:
                print("Error option")
        except Exception as e:
            print("Error:", e)
            break