a=int(input("enter 1st value"))
b=int(input("enter 2nd value"))
c=int(input("enter 3rd value"))
print(a,b,c)
if(a>b):
    if(a>c):
        print("1st value bigger")
if(b>a):
    if(b>c):
        print("2nd value bigger")

if(c>a):
    if(c>b):
        print("3rd is bigger")

