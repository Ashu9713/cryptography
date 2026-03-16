def encrypt(p,k):
    return p ^ k

def decrypt(c,k):
    return c ^ k

k=int(input("Enter key: "))
ch=input("Enter E for Encryption or D for Decryption: ")

if ch=="E":
    p=int(input("Enter plaintext: "))
    c=encrypt(p,k)
    print("Ciphertext:",c)

elif ch=="D":
    c=int(input("Enter ciphertext: "))
    p=decrypt(c,k)
    print("Plaintext:",p)
