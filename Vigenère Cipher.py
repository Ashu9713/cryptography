text = input("Enter text: ").upper()
key = input("Enter key: ").upper()
choice = input("E for Encrypt / D for Decrypt: ")

result = ""
k = 0

for c in text:
    shift = ord(key[k % len(key)]) - 65
    if choice == 'E':
        result += chr((ord(c)-65+shift) % 26 + 65)
    else:
        result += chr((ord(c)-65-shift) % 26 + 65)
    k += 1

print("Result:", result)
