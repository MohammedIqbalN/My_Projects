Num = input("Enter a number: ")

b = [x for x in range(1,100) if (x % Num) == 0]
print(b)