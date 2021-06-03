word = "ABABAB"
dict={}
for i in range (0,6):
    if (word[i] not in dict):
        dict[word[i]]=1
    else:
        print(word[i])
        break



