num=[[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
print(num)
for row in num:
    print(' |'+' |'.join(row)+' |')