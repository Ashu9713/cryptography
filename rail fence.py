def rail_fence(text, key):
    rail = [''] * key
    row, step = 0, 1

    for ch in text:
        if ch != " ":        # ignore spaces
            rail[row] += ch
            if row == 0:
                step = 1
            elif row == key - 1:
                step = -1
            row += step

    return ''.join(rail)

text = "HELLO WORLD"
key = 3

print("Encrypted:", rail_fence(text, key))
