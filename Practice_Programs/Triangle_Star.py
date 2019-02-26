l = 5
for i in range(6):
    if i != 0:
        print("")
    for k in range(l):
        print(" "),
    for j in range(i):
        print(" *"),
    l = l-1