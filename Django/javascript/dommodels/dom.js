//var htags=document.getElementsByTagName("h1")
//
//for (let tag of htags){
//    tag.style.color="red"
//}
//
//var litags=document.getElementsByTagName("li")
//
//for(let tag of litags){
//    tag.style.color="blue"
//}
//
//let hone=document.getElementById("hone")
//hone.style.color="green"
//
//var ltt=document.getElementsByClassName("ltt")
//for(let tag of ltt){
//    tag.style.color="pink"
//}

let qsl=document.querySelectorAll("li")
for(let tag of qsl){
    tag.style.color="green"
}

let hone=document.querySelectorAll("h1")
for(let tag of hone){
    tag.style.color="red"
}

let htwo=document.querySelector("#hone")
htwo.style.color="yellow"

let hon=document.querySelectorAll(".ltt")
for(let tag of hon){
    tag.style.color="orange"
}

let hm=document.querySelector("#hone")
//let data=hm.textContent
//alert(data)
hm.textContent="Dom Atribute"

//let hp=document.querySelectorAll(".ltt")
//for(let val of hp){
//    val.textContent="changed"
//}

//to pass with style
let hp=document.querySelectorAll(".ltt")
for(let val of hp){
    val.innerHTML="<em>changed</em>"
}
