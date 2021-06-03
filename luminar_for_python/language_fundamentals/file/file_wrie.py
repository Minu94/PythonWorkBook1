
#pgm to write sqares of no.s in a list to text file

f=open("give location here","w")
list2=[10,20,30,40]
squares=[(i**2) for in list2]
for val in squares:
    f.write(str(val)):
    f.write("\n")  #to write line by line

