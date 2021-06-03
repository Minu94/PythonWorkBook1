var txt=" ";

function disp(num){
    txt=document.querySelector("#inp")
    txt.value+=num


}

function solve(){
    var data=txt.value
    var res=eval(data)
    txt.value=res
}