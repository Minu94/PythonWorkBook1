
//single inheritance

class parent{
    phone(){
        console.log("havenokia")

    }
    class Child extends parent{
    }
}

var c=new Child();
c.phone()

//multilevel inheritance

class parent{
    m1(){
    console.log("m1")
    }
}

class Child extends parent{
    m2(){
    console.log("m2")
    }
}

class SubChild extends child{
    m3(){
    console.log("m3")
    }
}

//does not have multiple level inheritanc parent, child(parent),subchild(child,paarent)