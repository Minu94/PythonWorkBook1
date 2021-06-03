function add(num1,num2){
    num=num1+num2
}
//similar to lambda in python
// f = lambda x,y:x+y

var f=(num1,num2)=> num1+num2
console.log(f(1,50))

//cube of no.s

var cube=num=>num**3
console.log(cube(3))

//map function
//list(map( python

var arr=[2,4,56,7]
var squares = arr.map(num=>num**2)
console.log(squares)

// filter
var arr=[2,4,56,7]
var even=arr.filter(num=>num%2==0)
console.log(even)

//method for sorting
//no1>no2 put no1 first

var arr=[2,4,56,7]
var sorted=arr.sort(no1,no2)=>no1-no2
console.log(sorted)
//for descending

var arr=[2,4,56,7]
var sorted=arr.sort(no1,no2)=>no2-no1
console.log(sorted)

//reduce
//to find sum of element i arr

var total=arr.reduce(no1,no2)=>no1+no2
//max no
var heighest=arr.reduce(no1,no2)=>no1>no2?no1:no2
//1 and -1 can be used