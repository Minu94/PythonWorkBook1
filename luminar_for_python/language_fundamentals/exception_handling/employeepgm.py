try: #their is a chance of file not in the directory etc
    f=open("/home/user/Desktop/employee","r")
    emp={}
    for lines in f:
        line=lines.rstrip("\n").split(",")
        id=line[0]
        name=line[1]
        gender=line[2]
        desig=line[3]
        exp=line[4]
        emp[id]={"id":id,"name":name,"gender":gender,"desig":desig,"exp":exp}
except Exception as e:
    print(e.args)
print(emp["101"]["name"])


def printemployeedetails(**kwargs):
    if("id" in kwargs):
        id=kwargs["id"]
        print("id")
    if("prop" in kwargs):
        prop=kwargs["prop"]
        print(prop)
    print("employee with id",id,"property","name",emp[id]["name"])
    printemployeedetails(id="101",prop="desig")

