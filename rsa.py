import math
 
plaintext = int(input("Enter the message (integer) to be encrypted: "))
 
p = 101
q = 79
e = 11
 
n = p*q
 
def encrypt(plaintext):
    ciph = pow(plaintext, e, p*q)
    return ciph # ciph = (plaintext)^e % n

def decrypt(ciphertext):
    # phin = (p-1)*(q-1)
    # d = pow(e, -1, phin)
    # final = pow(ciphertext,d,n)
    # return final % n  
    d=pow(e,-1,(p-1)*(q-1))
    return pow(ciphertext,d,n)   

print("Original Plaintext Message is: ", plaintext)

ciph = encrypt(plaintext)
print(ciph)

decrypted = decrypt(ciph)

print("decrypted: " + str(decrypted))

#source code shamelessly stolen from https://www.pythonpool.com/rsa-encryption-python/