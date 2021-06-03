var clk=document.querySelector("#clk")
clk.addEventListener("click",()=>{
    clk.style.color="red"
})

//using defined function

//function clickedFn(){
//    clk.style.color="red";
//    clk.textContent="nothing"
//
//}
//clk.addEventListener("click",clickedFn)


let dbl=document.getElementById("dbl")
dbl.addEventListener("dblclick",()=>{
    dbl.style.color="brown"
    dbl.textContent="doubleclicked"
})

let hov=document.querySelector("#hov")
hov.addEventListener("mouseover",()=>{
 hov.style.color="blue"
 hov.textContent="over me"
})
hov.addEventListener("mouseout",()=>{
 hov.style.color="black"
 hov.textContent="out"
})