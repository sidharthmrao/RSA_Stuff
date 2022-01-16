import math
import keygen
 
def generate(length=1024):
    p,q,n,t,e,d = keygen.keygen(length)
    with open('values.txt', "w") as f:
        f.write(str(n)+"\n"+str(e)+"\n"+str(d))
    return n,e,d
def encrypt(plaintext):
    with open('values.txt',"r") as f:
        ned = f.readlines()
        n = int(ned[0].replace("\n",""))
        e = int(ned[1].replace("\n",""))
        d = int(ned[2].replace("\n",""))
    encrypted = pow(plaintext, e , n)
    return encrypted
def decrypt(ciphertext):
    with open('values.txt',"r") as f:
        ned = f.readlines()
        n = int(ned[0].replace("\n",""))
        e = int(ned[1].replace("\n",""))
        d = int(ned[2].replace("\n",""))
    return pow(ciphertext, d, n)