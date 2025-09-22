a = int(input("Enter a number: "))
num = 1
for i in range(a):
    print(num, end=", " if i < a - 1 else "\n")
    num += 2
