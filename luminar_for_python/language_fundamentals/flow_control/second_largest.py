num1=int(input("enter first no: "))
num2 =int(input("enter second no: "))
num3 = int(input("enter third no: "))
if((num1>num2)&(num1>num3)):
    if(num2>num3):
        print(num2,"2 nd largest")
    else:
        print(num3,"2 nd largest")
elif((num2>num3)&(num2>num1)):
    if(num3>num1):
        print(num3,"2 nd largest")
    else:
        print(num1,"2 nd largest")
elif((num3>num2)&(num3>num1)):
    if(num2>num1):
        print(num2,"2 nd largest")
    else:
        print(num1,"2 nd largest")
elif((num1==num2)&(num2==num3)):
    print("given no.s are equal")
else:
    pass







print()
