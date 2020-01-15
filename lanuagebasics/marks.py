a=int(input("enter 1st mark" ))
b=int(input("enter 2nd mark" ))
c=int(input("enter 3rd mark" ))

d=a+b+c
print ("Total = ",d)
if(d>145):
    print("A+")
if((d>140)&(d<=145)):
    print("A")
if((d>135)&(d<=140)):
    print("B+")
if((d>=130)&(d<135)):
    print("B")
if(d<130):
    print("Fail")