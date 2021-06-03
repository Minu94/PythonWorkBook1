if (condition){
};
else{
}
var num=10;
if(num<0){
console.log("negative")
}
else{
console.log("positive")
}

//odd -eve

var num=Number(prompt("number"));
if(num%2==0){
console.log("even")
}
else{
    console.log("odd")
}


//using prompt similar to python input
//for that first link to html page
var num =Number(prompt("number"));
var flag=0;
for (var i=2;i<num;i++){
    if (num%i==0){
        flag+=1;
        break;
    }
    else{
    flag=0
    }
}
if (flag===0){
(alert("not prime"))
}
else{
alert("prime")
}
//  to get type
js has no integer float seperation both are numbers
var num1=10
console.log(typeof(num1))
//
//== used for content matching not for data type matching
//=== used for matching both content and type matching
var num=10
var data="10"
if (num==data){
console.log("both are equal")
}
    else{
    console.log("not equal")
    }
it result will be equal since content are equal
//max among three number

var num1=10
var num2=11
var num3=9
if(num1>num2 & num1>num3){
    console.log("largest "+num1)
}
if(num2>num1 & num2>num3){
    console.log("largest"+num2)
}
if(num3>num1 & num3>num2){
    console.log("largest"+num3)
}

// javascript data type typeof
number
string
boolean (var name=true;)
undefined (if var is not used)

//terinary
if else, if elseif else
while