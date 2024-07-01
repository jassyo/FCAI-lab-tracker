let labEditForm = document.getElementById("lab_edit");
let labHead = document.getElementById("lab_header");
let labId = document.getElementById("lab_id_input");
let labName = document.getElementById("lab_name_input");
let labBuilding = document.getElementById("lab_building_input");
let labFNumber = document.getElementById("lab_floor_number_input");
let labPcsCount = document.getElementById("lab_pc_count_input");
let labChairsCount = document.getElementById("lab_chair_count_input");
let labStatus = document.getElementById("lab_status_input");
let pcEditForm = document.getElementById("pc_edit");
let pcHead = document.getElementById("pc_header");
let pcId = document.getElementById("pc_id_input");
let pcLabId = document.getElementById("pc_lab_id_input");
let pcStatus = document.getElementById("pc_status_input");
let pcComment = document.getElementById("pc_comment_input");
let btnAdd = document.getElementById("add");
let btnUpdate = document.getElementById("update");
let btnDelete = document.getElementById("delete");

const urlParams = new URLSearchParams(window.location.search);
const page_type = urlParams.get("type");
const pcIdInput = urlParams.get("pcId");
const labIdInput = urlParams.get("labId");

let labFields = [
  labId,
  labName,
  labBuilding,
  labFNumber,
  labPcsCount,
  labChairsCount,
  labStatus,
];
let pcFields = [pcId, pcLabId, pcStatus,pcComment];

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

  page_type === "l" ? (
    pcEditForm.style.display = "none", pcHead.style.display = "none",

    labData = await fetch(`http://127.0.0.1:8000/get/lab?labId=${labIdInput ?? 0}`)
      .then((data) => data.json())
      .then((data) => data[0]),

  Object.keys(labData).forEach((key, index) => (labFields[index].value = labData[key]))): 0;

  page_type === "p" ? (
    labEditForm.style.display = "none", labHead.style.display = "none",

    pcData = await fetch(`http://127.0.0.1:8000/get/pc?pcId=${pcIdInput ?? 0}`)
      .then((data) => data.json())
      .then((data) => data[0]),

    Object.keys(pcData).forEach((key, index) => (pcFields[index].value = pcData[key]))): 0;

  ((pcIdInput != null && page_type == "p") ||
    (labIdInput != null && page_type == "l"))? (btnAdd.style.display="none"):(0)

}

async function addFunction(){
  let pcData = {
    labId: pcFields[1].value,
    pcStatus: pcFields[2].value,
    comment: pcFields[3].value,
  };

  let labData = {
    labName: labFields[1].value,
    labBuilding: labFields[2].value,
    labFNumber: parseInt(labFields[3].value),
    labPcsCount: parseInt(labFields[4].value),
    labChairsCount: parseInt(labFields[5].value),
    labStatus: labFields[6].value,
  };

  if(page_type == "p"){

    const csrfToken = getCookie("csrftoken");
    fetch("http://127.0.0.1:8000/post/pc", {
      method: "POST",
      headers: { "X-CSRFToken": csrfToken },
      body: JSON.stringify(pcData),
    })
      .then((data) => data.json())
      .then((data) => console.log(data));

  } else if(page_type == "l"){
    
    const csrfToken = getCookie("csrftoken");
    fetch("http://127.0.0.1:8000/post/lab", {
      method: "POST",
      headers: { "X-CSRFToken": csrfToken },
      body: JSON.stringify(labData),
    })
      .then((data) => data.json())
      .then((data) => console.log(data));

  }
  alert("this object have been added succesfully!")
}

async function updateFunction(){
    let pcData = {
      pcId: pcFields[0].value,
      labId: pcFields[1].value,
      pcStatus: pcFields[2].value,
      comment: pcFields[3].value,
    };

    let labData = {
      labId: labFields[0].value,
      labName: labFields[1].value,
      labBuilding: labFields[2].value,
      labFNumber: parseInt(labFields[3].value),
      labPcsCount: parseInt(labFields[4].value),
      labChairsCount: parseInt(labFields[5].value),
      labStatus: labFields[6].value,
    };

    page_type == "p" ? (
      (csrfToken = getCookie("csrftoken")),
      fetch("http://127.0.0.1:8000/update/pc", {
          method: "POST",
          headers: { "X-CSRFToken": csrfToken },
          body: JSON.stringify(pcData),
      })
      .then((data) => data.json())
      .then((data) => console.log(data)))
          : 0;

      page_type == "l" ? (
      (csrfToken = getCookie("csrftoken")),
      fetch("http://127.0.0.1:8000/update/lab", {
            method: "POST",
            headers: { "X-CSRFToken": csrfToken },
            body: JSON.stringify(labData),
        })
        .then((data) => data.json())
        .then((data) => console.log(data)))
        : 0;
        alert("this object have been updated succesfully!");
        window.location.reload();
}

async function deleteFunction(){
      page_type == "p"
        ? fetch(`http://127.0.0.1:8000/delete/pc?pcId=${pcFields[0].value}`)
            .then((data) => data.json())
            .then((data) => console.log(data))
        : 0;

      page_type == "l"
        ? fetch(`http://127.0.0.1:8000/delete/lab?labId=${labFields[0].value}`)
          .then((data) => data.json())
          .then((data) => console.log(data))
        : 0;

        alert("this object have been removed succesfully!");
        window.location.reload();
}
btnAdd.addEventListener("click",addFunction)
btnUpdate.addEventListener("click", updateFunction)
btnDelete.addEventListener("click", deleteFunction)
setDefaultState();
