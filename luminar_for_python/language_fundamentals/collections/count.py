list1 = [10, 20, 50, 30, 40, 50, 50]
dict={}
for i in list1:
    if (i not in dict):
        dict[i]=1
    else:
        dict[i]+=1
print(dict)
print("count of 50=",dict[50])


