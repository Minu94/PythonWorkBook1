dict={}
for num in list:
    if (num not in dict):
        dict[num]+=1
for k,v in dict.items(): #linear search
    print(k,",",v)
element=int(input("entert num"))
if (element in dict):
else:
    print("not in dict")


element=int(input("element"))
flg=0
for val in list:
    if(element==val):
        flg+=1
         break
else:

