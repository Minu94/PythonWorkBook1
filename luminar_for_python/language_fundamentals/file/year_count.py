f1 = open("/home/user/Downloads/sampless/movies.csv","r")
dict={}
for data in f1:
    data2=data.rstrip("\n").split(",")
    year=list(filter(lambda word:word==data2[2],data2))
    for yr in year:
        if (yr not in dict ):
            dict[yr]=1
        else:
            dict[yr]+=1
for k,v in dict.items():
    print(k,",",v)


