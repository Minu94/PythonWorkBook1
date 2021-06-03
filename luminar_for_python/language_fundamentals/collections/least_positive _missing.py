list2=[3,4,0,9,10,-2,0,-5,-6]
list2.sort()
dict={}
for i in list2:
    if (i>=0)&(i+1 in list2):
        dict[i]="True"
    elif(i<0):
        dict[i]="True"
    else:
        print("least +ve inger missing: ",i+1)
        break
for i in range(0,len(list2)):
    if(num in list):


