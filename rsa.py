import math
import keygen

def generate(length=1024):
    p,q,n,t,e,d = keygen.keygen(length)
    with open('values.txt', "w") as f:
        f.write(str(n)+"\n"+str(e)+"\n"+str(d))
    return n,e,d

def encrypt(plaintext):
    plaintext = plaintext.replace("\n","").replace(" ","").replace("-","").replace("_","").replace(".","").replace(",","").replace("'","").replace("?","").replace("!", "")
    plain = ""
    for character in plaintext:
        if len(str(ord(character))) == 2:
            plain+=str(ord(character))
        else:
            plain += str(ord(character))
    plain = int(plain)
    with open('values.txt',"r") as f:
        ned = f.readlines()
        n = int(ned[0].replace("\n",""))
        e = int(ned[1].replace("\n",""))
        d = int(ned[2].replace("\n",""))
    encrypted = pow(plain, e , n)
    return encrypted 

def decrypt(ciphertext):
    with open('values.txt',"r") as f:
        ned = f.readlines()
        n = int(ned[0].replace("\n",""))
        e = int(ned[1].replace("\n",""))
        d = int(ned[2].replace("\n",""))
    decrypted = pow(ciphertext, d, n)
    plain = [(str(decrypted)[i:i+3]) for i in range(0, len(str(decrypted)), 3)]
    out = ""
    for i in plain:
        out+=chr(int(i))
    print(out)
    return out

a = encrypt("sir-this-is-a-test")
print(a)
b = decrypt(a)