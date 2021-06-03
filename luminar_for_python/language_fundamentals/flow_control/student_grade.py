name = input("student name: ")
mark1 = int(input("student mark for sub1: "))
mark2 = int(input("student mark for sub2: "))
mark3 = int(input("student mark for sub3: "))
total=mark1+mark2+mark3
if(total>=145):
    print(name,"got A+ grade")
elif((total>=140)&(total<145)):
    print(name,"got A grade")
elif((total>=135)&(total<140)):
    print(name,"got B+ grade")
elif((total>=130)&(total<135)):
    print(name,"got B grade")
elif((total>=125)&(total<130)):
    print(name,"got c grade")
else:
    print(name,"failed")




