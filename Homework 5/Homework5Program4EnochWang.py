# Enoch Wang
# 2/26/2020
# Homework 5 Program 4
# CSCI 6651
# Professor Gulnora Nurmatova 
# Resource https://devqa.io/encrypt-decrypt-data-python/

import unittest
from cryptography.fernet import Fernet

# A global variable key was used to ensure a consistent encryption and decryption
# Ensuring the same key is stored somewhere is important so that we able to decrypt our message
# Storing the key in a global variable is far less secure than generating one in a file;
# However, as the encryption is simple proof of concept it will suffice for our purposes
key = Fernet.generate_key()
inmessage = ""
outmessage = ""

def test():
    val = input("Enter a String: ")
    return val

def integer_test():
    return "112358132134"
    
def encrypt(r):
    def inner():
        s = r()
        encode = s.encode()
        f = Fernet(key)
        encrypted = f.encrypt(encode)
        inmessage = encrypted.decode("UTF-8")
        return inmessage
    return inner

def decrypt(r):
    def inner():
        s = r()
        f = Fernet(key)
        s = bytes(s, "UTF-8")
        decrypted = f.decrypt(s)
        return decrypted.decode("UTF-8")
    return inner
    
class TestEncryption(unittest.TestCase):     

    def test_auto(self):
        encrypt(integer_test)
        decrypt(integer_test)
        self.assertEqual(inmessage, outmessage)

if __name__ == '__main__': 
    
    unittest.main()

    dec = encrypt(test)
    res = dec()
    print(res)
    dec = decrypt(test)
    res = dec()
    print(res)