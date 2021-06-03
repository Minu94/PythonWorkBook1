list2=[5,1,7,2,4]
# list2.sort()
# list2
# num=int(input("enter an element"))
# for i in list2:
#     for j in list2:
#         if (i+j==num) & (j<=i):
#              print((i,j))

list2.sort()
list1=[]
low=0
upper=len(list2)-1
while(low<=upp):
    sum=list2[low]+list2[upper]
    if(sum==num):
        print(list1.append((list2[low],list2[upper])))
        low+=1
        break
    if (sum<element):
        low+=1
    elif sum>element:
        upper-=1
    else:
        pass



