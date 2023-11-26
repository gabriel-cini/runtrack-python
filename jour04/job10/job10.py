L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]


prdc= 1

for elmn in L:

    if elmn >= 25 and elmn <= 90:
     prdc *= elmn

print(prdc)