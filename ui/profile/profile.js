const myForm = document.getElementById("login_form");
const msgOk = document.getElementById("msg-ok");
const msgErr = document.getElementById("msg-err");
const loading = document.getElementById("loading");
const user = document.getElementById("user");
const asked = document.getElementById("asked");
const answered = document.getElementById("answered");
const ms = document.getElementById("ms");
const qs = document.getElementById("qs");
const url = "https://questioner2.herokuapp.com/api/v2/profile";
// const url = "http://127.0.0.1:5000/api/v2/profile";

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
        user.innerHTML = data.data[0].user_email;
        asked.innerHTML = data.data[0].asked;
        answered.innerHTML = data.data[0].answered;

        let meetups = data.data[0].meetups;
        let questions = data.data[0].top_questions;

        meetups.forEach(({ m_date, m_title }) => {
          ms.innerHTML += `<li class="feed-item">
                    <time class="date">${m_date}</time>
                    <span class="text"><a href="#">“${m_title}”</a></span>
                </li>`;
        });

        questions.forEach(({ q_date, q_title }) => {
          qs.innerHTML += `<li class="feed-item">
                    <time class="date">${q_date}</time>
                    <span class="text">New question: <a href="#">“${q_title}”</a></span>
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
