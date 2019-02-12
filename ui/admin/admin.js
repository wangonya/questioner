const myForm = document.getElementById("login_form");
const user = document.getElementById("user");
const posted = document.getElementById("posted");
const ms = document.getElementById("ms");
const qs = document.getElementById("qs");
// const url = "https://questioner2.herokuapp.com/api/v2/admin";
const url = "http://127.0.0.1:5000/api/v2/admin";

function getAdminData() {
  if (sessionStorage.accessToken) {
    loading.className = "show";
    setTimeout(() => {
      loading.className = loading.className.replace("show", "");
    }, 15000);
    fetch(url, {
      headers: new Headers({
        Authorization: `Bearer ${sessionStorage.accessToken}`
      })
    })
      .then(response => response.json())
      .then(data => {
        loading.className = loading.className.replace("show", "");
        if (data.status === 200) {
          user.innerHTML = data.data[0].admin_email;
          posted.innerHTML = data.data[0].meetups_posted;

          let meetups = data.data[0].meetups;
          let questions = data.data[0].questions;

          meetups.forEach(({ happening_on, title, id }) => {
            ms.innerHTML += `<li class="feed-item">
                    <time class="date">${happening_on}</time>
                    <span class="text"><a href="#">“${title}”</a>
                    <a href="#open-modal" onclick="setDeleteId(${id})"><i class="far fa-trash-alt" title="Delete this meetup"></i></a></span>
                </li>`;
          });

          questions.forEach(({ q_date, q_title }) => {
            qs.innerHTML += `<li class="feed-item">
                    <time class="date">${q_date}</time>
                    <span class="text"><a href="#">“${q_title}”</a></span>
                </li>`;
          });
        } else {
          msgErr.className = "show";
          setTimeout(() => {
            msgErr.className = msgErr.className.replace("show", "");
          }, 4000);
          msgErr.innerHTML = "An error occurred while fetching your data";
        }
      });
  } else {
    window.location.replace("../login");
  }
}

function setDeleteId(id) {
  sessionStorage.delete_id = id;
}

function deleteMeetup() {
  // const deleteUrl = `https://questioner2.herokuapp.com/api/v2/meetups/${sessionStorage.delete_id}`;
  const deleteUrl = `http://127.0.0.1:5000/api/v2/meetups/${
    sessionStorage.delete_id
  }`;
  fetch(deleteUrl, {
    method: "DELETE",
    headers: new Headers({
      Authorization: `Bearer ${sessionStorage.accessToken}`
    })
  })
    .then(response => response.json())
    .then(data => {
      loading.className = loading.className.replace("show", "");
      if (data.status === 200) {
        msgOk.className = "show";
        setTimeout(() => {
          msgOk.className = msgOk.className.replace("show", "");
        }, 4000);
        msgOk.innerHTML = "";
        msgOk.innerHTML = data.data[0].message;
        ms.innerHTML = "";
        getAdminData();
      } else {
        msgErr.className = "show";
        setTimeout(() => {
          msgErr.className = msgErr.className.replace("show", "");
        }, 4000);
        msgErr.innerHTML = data.message;
      }
    });
  window.location.replace("#");
}
