##list comprehension

lst1=[1,2,3]
lst2=[4,5,6]
## pgm to print all combination of (1,2),(1,3),(1,4) etc

for i in lst1:
    for j in lst2:
        print((i,j))
## above pgm using list comprehension

data=[(i,j) for i in lst1 for j in lst2]
print(data)

# # caculating square of element of list2

square=[(i*i) for i in lst1]
print(square)
# # even nos

even=[i for i in lst1 if i%2==0]
print(even)
# even squares

square=[i*i for i in lst1 if i%2==0]
print(square)