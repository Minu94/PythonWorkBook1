
# for giving any no of arguments

def varArgMeth(**kwargs):#can recieve any no of argument
    print(type(kwargs)) #dictionary - kwargs is in the form of dictionary
    for k,v in kwargs.items():
        print(k,"->",v)

varArgMeth(name="abc",age=25)