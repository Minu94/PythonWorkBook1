file=open("/home/user/Downloads/hotels.csv","r")


def get(state,field,operation):
    dict_line=[0]
    hotels={}
    for position,row in enumerate(file):
        if position in dict_line:
            data=row.rstrip("\n").split(",")
            for i in range(1,len(data)):
                hotels[data[i]]=[]
            hotels["Rating"]=hotels.pop("Ratings")
        else:
            data=row.rstrip("\n").split(",")
            for i in range(1,len(data)):
                if state.capitalize() in data:
                    for num,keys in enumerate(hotels.keys()):
                        if (i-1) == num:
                            hotels[keys].append(data[i])
    request_data=hotels[field.capitalize()]
    request_data=[float(i) for i in request_data]

    def hotel_code(value):
        ls=[]
        for i in range(len(request_data)):
            if value==request_data[i]:
                ls.append(hotels["Hotel Code"][i])
        return ls
    if operation=="cheapest":
        value = min(request_data)
        for code in hotel_code(value):
            print(f"Hotel with cheapest {field} in {state.capitalize()} is {code} with {field} {value}")
    elif operation =="highest":
        value = max(request_data)
        for code in hotel_code(value):
            print(f"Hotel with highest {field} in {state.capitalize()} is {code} with {field} {value}")
    elif operation =="average" :
        value=(sum(request_data))/(len(request_data))
        print(f"Average rating of Hotel in {state} is {value}")
    else:
        print("wrong input")


state=input("state: " )
field=input("Cost or Rating: ")
operation=input("operation: ")
get(state,field,operation)





