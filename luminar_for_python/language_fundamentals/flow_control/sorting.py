num1 = int(input("give first no: "))
num2 = int(input("give second no: "))
num3 = int(input("give third no: "))
if(num1>=num2>=num3):
    print("after sorting",num3,num2,num1,sep='\n')
elif(num1>=num3>=num2):
    print("after sorting",num2,num3,num1,sep='\n')
elif(num2>=num1>=num3):
    print("after sorting",num3,num1,num2,sep='\n')
elif(num2>=num3>=num1):
    print("after sorting",num1,num3,num2,sep='\n')
elif(num3>=num1>=num2):
    print("after sorting",num2,num1,num3,sep='\n')
elif(num3>=num2>=num1):
    print("after sorting",num1,num2,num3,sep='\n')
else:
    pass