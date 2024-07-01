fetch("http://127.0.0.1:8000/get/labs")
.then(function(response){
    return response.json();
})
.then(function(datas){
    let placeholde=document.querySelector("#mytable");
    let out="";
    for(let data of datas){
        out+=`
        <tr>
        <td>${data.id}</td>
        <td>${data.labBuilding}</td>
        <td>${data.labName}</td>
        <td>${data.labFNumber}</td>
        <td>${data.labPcsCount}</td>
        <td>${data.labStatus}</td>
        </tr>
        `
    }
    placeholde.innerHTML+=out;
})

fetch("http://127.0.0.1:8000/get/pc")
.then(function(res){
    return res.json();
})
.then(function(pcdata){
    let place=document.querySelector("#mytable1");
    let row="";
    for(let pc of pcdata){
        row+=`
        <tr>
        <td>${pc.labId}</td>
        <td>${pc.id}</td>
        <td>${pc.pcStatus}</td>
        <td>${pc.comment}</td>
        </tr>
        `
    }
    place.innerHTML+=row;
})



function show_labtable(){
    var variable1=document.getElementById('open1');
    var hide_show1=variable1.style.display=="none";
    if(hide_show1){
        variable1.style.display="table";

    }else{
        variable1.style.display="none";
    }
    
}
function show_pcstable(){
    var variable2=document.getElementById('open2');
    var hide_show2=variable2.style.display=="none";
    if(hide_show2){
        variable2.style.display="table";

    }else{
        variable2.style.display="none";
    }
    
}

