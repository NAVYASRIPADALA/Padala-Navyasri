a=int(input("Enter a number: "))
if a%2==0:
    n=a-1
else:
    n=a
count=1
num=1
while count<=n:
    if count==n:
        print(num)
    else:
        print(num, end=", ")
    num+=2
    count+=1