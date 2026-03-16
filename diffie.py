choice = input("Do you want to perform Diffie-Hellman key exchange? (yes/no): ")

if choice.lower() == "yes":

    p = int(input("Enter prime number (p): "))
    g = int(input("Enter primitive root (g): "))

    a = int(input("Enter private key of User A: "))
    b = int(input("Enter private key of User B: "))

    A = (g ** a) % p
    B = (g ** b) % p

    print("Public key of A:", A)
    print("Public key of B:", B)

    keyA = (B ** a) % p
    keyB = (A ** b) % p

    print("Secret key for A:", keyA)
    print("Secret key for B:", keyB)

else:
    print("Program terminated")
