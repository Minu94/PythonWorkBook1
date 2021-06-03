// class,object,reference

class person{
    setperson(age,name){
        this.age=age
        this.name=name
    }
    printperson(){
        console.log(this.age)
        console.log(this.person)
    }
}
//object
var obj=new person()
obj.setperson(25,"chinnu")
obj.printperson()

//set person intialize instnace variable (person has age,person has name)

//initialize instance variables:constructor
//so set person is a constructor
//so changed to
class person{
    constructor(age,name){
        this.age=age
        this.name=name
    }
    printperson(){
        console.log(this.age)
        console.log(this.person)
    }
}

var obj=new person(25,"chinnu")
obj.printperson()