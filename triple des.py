p=3
q=11
n=p*q
phi=(p-1)*(q-1)

e=7
for i in range(2,phi):
    if (e*i)%phi==1:
        d=i
        break

print("Public Key:",(e,n))
print("Private Key:",(d,n))

ch=input("Enter E for Encryption or D for Decryption: ")

if ch=="E":
    m=int(input("Enter message: "))
    c1=(m**e)%n
    c2=(c1**e)%n
    c3=(c2**e)%n
    print("Triple Encrypted message:",c3)

elif ch=="D":
    c=int(input("Enter cipher: "))
    m1=(c**d)%n
    m2=(m1**d)%n
    m3=(m2**d)%n
    print("Triple Decrypted message:",m3)
