let employee =[{},{},{}]


for (let emp of employee){
console.log(emp.desig+','+emp.name)
}
//while using let it has scope inside only in for loop

//it is similar to

employee.forEach(emp=>console.log(emp.desig+','+emp.name))


logical boolean operator &&

var employee=employee.filter(emp=>(emp.join>=1990 && emp.join<=2000))