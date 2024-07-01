let labInfo = document.getElementById("lab_info_container");
let labId = document.getElementById("lab_id_data");
let labName = document.getElementById("lab_name_data");
let labBuilding = document.getElementById("lab_building_data");
let labFNumber = document.getElementById("lab_floor_number_data");
let labPcsCount = document.getElementById("lab_pc_count_data");
let labChairsCount = document.getElementById("lab_chair_count_data");
let labStatus = document.getElementById("lab_status_data");
let pcInfo = document.getElementById("pc_info_container");
let pcId = document.getElementById("pc_id_data");
let pcLabId = document.getElementById("pc_lab_id_data");
let pcStatus = document.getElementById("pc_status_data");
let pcComment = document.getElementById("pc_comment_data");
let pcIdUserInput = document.getElementById("pc_id_input");
let pcIdSubmit = document.getElementById("pc_id_submit");

let btnSubmit = document.getElementById("pc_id_submit");

const urlParams = new URLSearchParams(window.location.search);
const pcIdInput = urlParams.get("pcId");

let labFields = [labId,labName,labBuilding,labFNumber,labPcsCount,labChairsCount,labStatus]
let pcFields = [pcLabId,pcId, pcStatus, pcComment];

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue; 
  }
  

async function setDefaultState() {
  let pcData = await fetch(`http://127.0.0.1:8000/get/pc?pcId=${pcIdInput}`)
    .then((data) => data.json())
    .then(data=>data[0])

  let labData = await fetch(`http://127.0.0.1:8000/get/lab?pcId=${pcIdInput}`)
      .then((data) => data.json())
      .then((data) => data[0]);

    Object.keys(labData).forEach(
      (key, index) => (labFields[index].innerText = labData[key])
    );

    console.log("DATA",pcData,labData)
    Object.keys(pcData).forEach(
      (key, index) => (pcFields[index].innerText = pcData[key])
    );
}

function getRadioValue(){
    let value;
    radios.forEach(
         (e)=>(e.checked === true ? (value = e.value): (0) )
     )
     return value;
}



function updateURL(){
  window.location.search =`?pcId=${pcIdUserInput.value}`
}

btnSubmit.addEventListener("click",getRadioValue);

pcIdSubmit.addEventListener("click",updateURL)
setDefaultState()
