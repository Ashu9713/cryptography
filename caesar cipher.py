text = input("Enter text: ").upper()
key = int(input("Enter key: "))
choice = input("Type E for Encrypt or D for Decrypt: ")

result = ""

for c in text:
    if choice == 'E':
        result += chr((ord(c) - 65 + key) % 26 + 65)
    elif choice == 'D':
        result += chr((ord(c) - 65 - key) % 26 + 65)

print("Result:", result)
