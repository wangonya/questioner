const msgOk = document.getElementById("msg-ok");
const msgErr = document.getElementById("msg-err");
const loading = document.getElementById("loading");
const main = document.getElementById("main");
const featured = document.getElementById("featured");

// load upcoming meetups on home page
function getUpcomingMeetups() {
  const url = "https://questioner2.herokuapp.com/api/v2/meetups/upcoming";
  // const url = "http://127.0.0.1:5000/api/v2/meetups/upcoming";
  loading.className = "show";
  setTimeout(() => {
    loading.className = loading.className.replace("show", "");
  }, 15000);
  fetch(url)
    .then(response => response.json())
    .then(data => {
      loading.className = loading.className.replace("show", "");
      if (data.status === 200) {
        let main_meetup = data.data[0];
        let meetups = data.data.slice(1);

        featured.innerHTML = `<div class="grid-item main">
            <img src="${main_meetup.image}" alt="meetup image" />
            <div class="text-block">
              <a href="javascript:goToSpecificMeetup(${main_meetup.id})"><h2>${
          main_meetup.title
        }</h2></a>
              <small>${main_meetup.happening_on}</small>
              <br />
              <p>
                ${main_meetup.details}
              </p>
            </div>
          </div>`;

        meetups.forEach(({ title, happening_on, id, image }) => {
          featured.innerHTML += `<div class="grid-item featured">
            <img src="${image}" alt="meetup image" />
            <div class="text-block">
              <a href="javascript:goToSpecificMeetup(${id})"><h4>${title}</h4></a>
              <small>${happening_on}</small>
            </div>
          </div>`;
        });
      } else {
        msgErr.className = "show";
        setTimeout(() => {
          msgErr.className = msgErr.className.replace("show", "");
        }, 4000);
        msgErr.innerHTML = data.message;
      }
    });
}
function goToSpecificMeetup(id) {
  window.location.replace("meetup/");
  window.sessionStorage.m_id = id;
}
