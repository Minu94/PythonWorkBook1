//value in " not key
person = {name:"chinnu",age :12,salary:3000}
//while fetching use ""
console.log(person["name"])
console.log(person["salary"])
//changing value

person["salary"]+=5000
console.log(person.salary)
//boolean
console.log(gender in person)
//adding key
person.gender = "male";
console.log(person)
//counting letters in words
var text="how are you"
var words=text.split(" ")
var dict={}
for (letter in words){
    if(letter in dict){
        dict.letter+=1
    }
    else{
    dict.letter=1
    }
}
console.log(dict)