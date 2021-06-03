#create file with words
## hai hello how are you
## fine hello how are you etc...
#and count the words

f=open("file location","w")
dict{}
for lines in f1:
    words=lines.rstrip("\n"),split(" ")
    for word in words:
        if word not in dict:
            dict[word]=1
        else:
            dict[word]+=1
for k,v in dict.items():
    print(k,",",v)