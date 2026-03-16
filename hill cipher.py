# Key matrix values
a, b, c, d = 3, 3, 2, 5

text = "HELLO"

if len(text) % 2 != 0:
    text += "X"

result = ""

for i in range(0, len(text), 2):
    x = ord(text[i]) - 65
    y = ord(text[i+1]) - 65

    r1 = (a*x + b*y) % 26
    r2 = (c*x + d*y) % 26

    result += chr(r1 + 65) + chr(r2 + 65)

print("Encrypted:", result)
