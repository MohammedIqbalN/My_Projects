l = 5
for i in range(6):
    if i != 0:
        print("")
    for k in range(l):
        print(" "),
    for j in range(i):
        print(" * "),
    l = l-1
l = 1
for i in range(5,0,-1):
    print("")
    for k in range(l):
        print(" "),
    for j in range(i):
        if j != 0:
            print(" * "),
    l = l+1
