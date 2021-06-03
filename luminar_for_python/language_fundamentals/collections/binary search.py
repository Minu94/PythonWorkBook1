# (in dict we use linear search)
# binary search example


list1=[10,23,45,67,12,13,67]
list1.sort() #sort and store the value to list1 itself , here list1 becomes list1=[10,12,13,23,45,67,67]
low=0
upp=len(list1)
element=int(input("give element"))    #let element be 45
flg=0
while(low<upp):                   # mid here3 len start from1(low=0,upp=6,mid=0+6/2
    mid=(low+upp)//2
    if(element>list1[mid]):        #45>23
        low=mid+1                  #low=4
    elif(element<list1[mid]):      #false
        upp=mid-1
    elif(element==list1[mid]):      #false  goes to loop again
        flg+=1
        break
if(flg>0):
    print("element found")
else:
    print("not found")

