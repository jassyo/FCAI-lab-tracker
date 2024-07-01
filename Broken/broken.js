const tableContainer = document.querySelector("#tbody");
const btn = document.querySelector("#btn--click");
const input = document.querySelector("#input");
const form = document.querySelector("#form");

const getDate = async function (url) {
  const response = await fetch(url);
  const data = await response.json();
  return data;
};

let dataFetched = getDate("http://127.0.0.1:8000/get/pc");

async function init() {
  let idx = 0;
  let dataFetched = await getDate("http://127.0.0.1:8000/get/pc");
  dataFetched = dataFetched.filter((arrEl) => arrEl.pcStatus === "not working");
  dataFetched.forEach((arrEl, idx) => {
    const markUp = `
    <tr id=${arrEl.id}>
    <td>${idx + 1}</td>
    <td><a href="../Edit./Edit.html?type=p&pcId=${arrEl.id}">${arrEl.id}</a></td>
    <td><a href="../Edit./Edit.html?type=l&labId=${arrEl.labId}">${arrEl.labId}</a></td>
    <td>${Math.floor(Math.random() * 2) ? "hardware" : "software"}</td>
    <td>${arrEl.comment}</td>
    </tr>
    `;
    tableContainer.insertAdjacentHTML("beforeend", markUp);
  });
};

init();

form.addEventListener("submit", function (e) {
  e.preventDefault();
  const value = input.value;

  let node = document.getElementById(value);
  if (node == null) alert("This computer ID isn't in the list!");
  else {
    let pcData = {
      pcId: node.id,
      pcStatus: "working",
      comment: "working again!",
    };

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
    const csrfToken = getCookie("csrftoken");
    fetch("http://127.0.0.1:8000/update/pc", {
      method: "POST",
      headers: { "X-CSRFToken": csrfToken },
      body: JSON.stringify(pcData),
    })
      .then((data) => data.json())
      .then((data) => console.log(data));

    console.log(node);
    tableContainer.removeChild(node);
    input.value = "";
    tableContainer.innerHTML = "";
    init();
  }
});
