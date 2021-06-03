list2=[2,3,4,5]
#file not found exception,sql exception it all comes under a class named exception
indx=int(input("print index position for fetching")) #
num1=int((input("no")))
num2=int((input("no")))
try:
    res=num1/num2
    print("i have 1 database")
except Exception as e:
    print(e.args)
try:
    print("element in the position",list2[indx])
except Exception as e:
    print(e.args)
#exception can occur in exception block
except Exception as e:
    print()
    try:
        f=open()
finally:#it will execute wheter there is exception or not/code that need to be executed mandatedly
    print()