class MyBank {

    static getUser(){
        var user={
            userone:{username:"userone",password:"one",accno:1000,balance:500},
            usertwo:{username:"usertwo",password:"two",accno:1001,balance:5001},
            userthree:{username:"userthree",password:"three",accno:1002,balance:5002}
        }
        return user

    }
    static login() {
        let username=document.querySelector("#username").value
        let password=document.querySelector("#pwd").value
        let users=MyBank.getUser()
        if (username in users){
            if (password==users[username]["password"]){
                alert("login successful")
                window.location.href="userhome.html"
            }
            else{
                alert("invalid password")
            }
        }
        else{
            alert("invalid username")
        }
    }
    static deposit(){
        let username=document.querySelector("#username").value
        let amnt=Number(document.querySelector("#amount").value)
        let users=MyBank.getUser()
        if (username in users){
            users[username]["balance"]+=amnt
            alert(users[username]["balance"])
        }
        else{
         alert("invalid username")
        }


    }
    static withdraw(){
        let username=document.querySelector("#username").value
        let amnt=Number(document.querySelector("#amount").value)
        let users=MyBank.getUser()
        if (username in users){
            if (amnt>users[username]["balance"]){
                alert("insufficient balance")
            }
            else{
                users[username]["balance"]-=amnt
                alert(users[username]["balance"])
            }
        }
        else{
         alert("invalid username")
        }

    }

}

//since function inside a class cannot be called without creating instance,
//we cannot create instance in html
//hence use static