
#exception handling
##pgm: use case example pgm, here if we give zero to num2 the pgm get terminated


num1=int((input("enter num1")))
num2=int((input("enter num 2")))
res=num1/num2
print("i have 1 database")


## exception handling:: abnormal code where program get terminated,
# here we give zero to  num2 its an exception
# exception does not means an error
        # key words try,except,finally
## syntax format


# try:
    #doubtful code
#except:
        #handling code


# pgm: example here if we give zero to num2 we get exception message without terminating pgm

num1=int((input("enter num1")))
num2=int((input("enter num2")))
try:
    res=num1/num2
    print("i have 1 database")
except:
    print("exception occured")

