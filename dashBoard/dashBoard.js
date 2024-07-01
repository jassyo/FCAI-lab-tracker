let job = document.getElementById("title_input")
let name = document.getElementById("name_input")
let mail = document.getElementById("mail_input");
let id = document.getElementById("id_input");
let changeBtn = document.getElementById("chBtn");

let dummyData = {
    job:"student",
    name:"ahmed",
    mail:"ahmedahmed647@gmail.com",
    id:"20200999"
}

let inputs = [job,name,mail,id]

function setDefault(){
    Object.keys(dummyData).forEach((key,index)=>(inputs[index].value =dummyData[key]))
}
function toggleReadState(){
    mail.readOnly = !mail.readOnly
}

changeBtn.addEventListener("click",toggleReadState )

setDefault();