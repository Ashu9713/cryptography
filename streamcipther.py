key = int(input("Enter key: "))
ch = input("Enter E for Encryption or D for Decryption: ")

if ch == "E":
    p = input("Enter plaintext: ")
    c = ""
    for i in p:
        c += chr((ord(i) + key) % 256)
    print("Ciphertext:", c)

elif ch == "D":
    c = input("Enter ciphertext: ")
    p = ""
    for i in c:
        p += chr((ord(i) - key) % 256)
    print("Plaintext:", p)
