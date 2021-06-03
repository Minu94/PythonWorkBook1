num1=int(input("give first num"))
num2=int(input("give second num"))
num3=int(input("give second num"))
if((num1>num2) &(num1>num3) ):
    print(num1,"is greater")
elif((num2>num1)&(num2>num3)):
    print(num2,"is greater")
elif((num3>num1)&(num3>num2)):
    print(num3,"greater")
elif((num1==num2)&(num2==num3)):
    print("all no.s are equal")
else:
    pass