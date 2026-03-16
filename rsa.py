def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def mod_inverse(e,phi):
    for d in range(1,phi):
        if (e*d)%phi==1:
            return d

p=3
q=11
n=p*q
phi=(p-1)*(q-1)

e=7
while gcd(e,phi)!=1:
    e+=1

d=mod_inverse(e,phi)

print("Public Key:",(e,n))
print("Private Key:",(d,n))

choice=input("Enter E for Encryption or D for Decryption: ")

if choice=="E":
    m=int(input("Enter message: "))
    c=(m**e)%n
    print("Encrypted message:",c)

elif choice=="D":
    c=int(input("Enter cipher: "))
    m=(c**d)%n
    print("Decrypted message:",m)
