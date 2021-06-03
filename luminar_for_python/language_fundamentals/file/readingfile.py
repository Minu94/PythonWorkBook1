#read
## referenc=open("path","mode")
##mode=read(r),write(w),append(a)


# create a text file with employee details employee name,age,salary etc then print employee names only
f=open("/home/user/Desktop/employee","r")
for data in f:
#     print (data)    <= to see data in the text file
    person=data.rstrip("\n").split(",") #rstrip to remove \n since display line by line
    print(person[0])
