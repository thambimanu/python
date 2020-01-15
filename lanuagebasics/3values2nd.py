a=int(input("enter 1st value"))
b=int(input("enter 2nd value"))
c=int(input("enter 3rd value"))
print(a,b,c)
if((a>b)&(b>c)|(a<b)&(c>b)):
    print("2nd value between 1st and 3rd")
elif((a>b)&(c>a)|(a<b)&(a>c)):
    print("1st value between 1st and 3rd")
if((c<a)&(c>b)|(c>a)&(c<b)):
    print("3rd value between 1st and 2nd")
