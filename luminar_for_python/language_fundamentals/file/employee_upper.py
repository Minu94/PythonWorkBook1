# 1991 yr wise count movie realesed count  , in which yr most released,
f1 = open("/home/user/Downloads/sampless/movies.csv","r")
dict={}
for data in f1:
    data2=data.rstrip("\n").split(",")
    for words in data2:
        if (words==data2[2])&(words not in dict):
            dict[words]=1
        elif (words==data2[2])&(words in dict):
            dict[words]+=1
        else:
            pass
list1=[]
for k,v in dict.items():
    list1.append(v)
    list1.sort()
a=list1[-1]
for k,v in dict.items():
    if v==a:
        print(k)
    # print(data2[2])