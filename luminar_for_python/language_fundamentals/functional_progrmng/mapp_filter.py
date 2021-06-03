## map,filter
# # map() apply to each element(if we want to find square of each element in a list)
# map accept two argument :: function and iterable
# #filter not apply to each element (in a list if want to extract element of length 2)

lst=[10,20,21]
def squares(no):
    return no*no
data=list(map(squares,lst))  #squares-function,lst-iterable
print(data)


data=list(map(lambda no:no*no,lst))
print(data)

## filter

#pgm for obtaining even nos from list

def evenc(num):
    return num%2==0
evenlst=list(filter(evenc,lst))
print(evenlst)