print("select :   1-->cotton   2-->silk    3-->linen")
a=int(input())
print("enter the purchased amount")
pamt=float(input())
if((a==1)&(pamt>20000)):
    t=.9*pamt
elif((a==1)&(pamt>15000)&(pamt<20000)):
    t=.91*pamt
elif((a==1)&(pamt>14000)&(pamt<15000)):
    t=.93*pamt
elif(a==1)&(pamt<14000):
    t=.98*pamt
if ((a == 2) & (pamt > 20000)):
    t = .85 * pamt
elif ((a == 2) & (pamt > 15000) & (pamt < 20000)):
    t = .90 * pamt
elif ((a == 2) & (pamt > 14000) & (pamt < 15000)):
    t = .91 * pamt
elif (a == 2) & (pamt < 14000):
    t = .95 * pamt
if ((a == 3) & (pamt > 20000)):
    t = .85 * pamt
elif ((a == 3) & (pamt > 15000) & (pamt < 20000)):
    t = .90 * pamt
elif ((a == 3) & (pamt > 14000) & (pamt < 15000)):
    t = .91 * pamt
elif (a == 3) & (pamt < 14000):
    t = .95 * pamt
print("***********************")
print("discounted price= ",t)


print



