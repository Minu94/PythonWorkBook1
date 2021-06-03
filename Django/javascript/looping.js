// initialization
// condition checking
// loop body
//var i=0;
//while(i<10){
//    console.log(i)
//    i++
//}

//reversing

//var num=123;
//var res=0;
//while (num>0){
//    var digit = num % 10;
//    var res = res*10+digit
////    3
//    var num = Math.floor(num/10)
////    12
////    var num = num*10+res
//
//}
//console.log(res)

//sample 2 2+22=24
//sample 3 3+33+333=369
//sample 4 4+44+444+4444=
//
//2
//2+(2*10+2)
//3+(3*10+3)+3*100+33
//4*10^0+0+(4*10^1+4)+(4*100+44)+4*1000+444
//var num=4
//var start=0
//var res=0
//var total=0
//while(start<num){
//    res=num*(10**start)+res
//    total+=res
//    start++
//
//}
//console.log(total)

//for loop

//for(var i=0;i<=10;i++){
//console.log(i)
//}
var power = 2
var num1=2
var num2 =27
for(var i=1;i<=num2;i++){
    if (i**power>=num1 & i**power<=num2){
        console.log(i**power)
    }
}