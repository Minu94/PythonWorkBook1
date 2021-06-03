silk=print("enter 1 if clothe type is silk")
cotton=print("enter 2 if clothe type is cotton")
linen=print("enter 3 if clothe type is linen")
type_no=int(input("give cllothe type no: "))
cost_p=int(input("enter purchase amount"))
if (type_no==1):
    if(cost_p<3000):
        a+=7
        print("discount allowed=7% , amount to be paid =",b,)
    elif((cost_p>=3000) & (cost_p<4000)):
        print("discount allowed=7% , amounnt to be paid =",(cost_p)*(100-7)/100)
    elif((cost_p>=4000)&(cost_p<5000) ):
        print("discount allowed=9% , amounnt to be paid =",(cost_p)*(100-9)/100)
    elif(cost_p>=5000 ):
        print("discount allowed=15% , amounnt to be paid =",((cost_p)*(100 - 15))/100)
elif (type_no==2):
    if(cost_p<3000):
        print("discount allowed=3% , amount to be paid=",((cost_p)*(100-3))/100)
    elif((cost_p>=3000) & (cost_p<4000)):
        print("discount allowed=5% , amounnt to be paid =",((cost_p)*(100-5))/100)
    elif((cost_p>=4000)&(cost_p<5000) ):
        print("discount allowed =8% , amounnt to be paid =",(cost_p)*(100-8)/100)
    elif(cost_p>=5000 ):
        print("discount allowed=12% , amounnt to be paid =",(cost_p)*(100 - 12)/100)
elif(type_no==3):
    if(cost_p<3000):
        print("no discount allowed =0 , amount to be paid= ",cost_p)
    elif((cost_p>=3000) & (cost_p<4000)):
        print("discount allowed=5% , amounnt to be paid =",(cost_p)*(100-5)/100)
    elif((cost_p>=4000)&(cost_p<5000) ):
        print(" discount allowed = 7% , amounnt to be paid =",(cost_p)*(100-7)/100)
    elif(cost_p>=5000 ):
        print("discount allowed=10%,amounnt to be paid =",(cost_p)*(100 - 10)/100)
else:
    pass


