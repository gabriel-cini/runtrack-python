L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

s = 0

for nb in L:
    if nb % 2 == 0:
        s += nb

print(s)