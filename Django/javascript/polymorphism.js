// method overloading

class Math{
    add(){
    console.log("no arg method")
    }

    add(num1){
    console.log("single argument method")
    }

    add(num1,num2){
    console.log("multiple argument method")
    }
}
var obj=new Math()
obj.add(10)
//result two argu method
obj.add(10,20)
//result two arg method
//like method overloading in python last method is called

//method overriding

class parent{
    phone(){
        console.log("havenokia")

    }
    class Child extends parent{
        phone(){
        console.log("child has samsung")
        }
    }
}

var c=new Child();
c.phone()
