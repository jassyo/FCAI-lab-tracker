var attempt = 3; // Variable to count number of attempts.
// Below function Executes on click of login button.
let submitbtn = document.getElementById("submitbtn")
submitbtn.addEventListener ("click",validate)
async function validate(){
var username = document.getElementById("username").value;
var password = document.getElementById("pass").value;
let user = await fetch("http://127.0.0.1:8000/get/user?searchTerm="+ username).then(data=>data.json())
user=user[0];
console.log("user", user);
//if array empty alert name not found in data base
if (user == null){
    attempt --;// Decrementing by one.
    alert("Username not found in our database");
    alert("You have left "+attempt+" attempt;");
    
}
else{
    if (password == user.password){
    alert ("Login successfully");
    window.location = "../dashboard/dashBoard.html"; 
    return false;
    }
    else if(password != user.password){
        alert ("wrong password");
    }
}
// Disabling fields after 3 attempts.
if( attempt == 0){
    document.getElementById("username").disabled = true;
    document.getElementById("password").disabled = true;
    document.getElementById("submit").disabled = true;
    return false;
    }
}