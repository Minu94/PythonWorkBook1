list1 = [1,2,3,4,5,6]
odd_list=[]
even_list=[]
for i in list1:
    result=i**2
    if result%2==0:
        even_list.append(result)
    else:
        odd_list.append(result)
print("even_list=",even_list)
print("odd_list=",odd_list)