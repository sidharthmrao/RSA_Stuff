import math
import keygen
 
def generate(length=1024):
    p,q,n,t,e,d = keygen.keygen(length)
    return n,e,d
def encrypt(plaintext, e, n):
    encrypted = pow(plaintext, e , n)
    return encrypted
def decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)   