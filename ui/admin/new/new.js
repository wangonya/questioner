const myForm = document.getElementById("new-meetup-form");
const msgOk = document.getElementById("msg-ok");
const msgErr = document.getElementById("msg-err");
const loading = document.getElementById("loading");

function validate() {
  const title = document.getElementById("title");
  const details = document.getElementById("details");
  const location = document.getElementById("location");
  const date = document.getElementById("date");
  const tags = document.getElementById("tags");
  const image = document.getElementById("image");

  if (title.value.length < 10) {
    msgErr.className = "show";
    setTimeout(() => {
      msgErr.className = msgErr.className.replace("show", "");
    }, 4000);
    msgErr.innerHTML = "";
    msgErr.innerHTML = "Title must be at least 10 characters long";
    title.focus();
    return false;
  }

  if (tags.value.length < 2) {
    msgErr.className = "show";
    setTimeout(() => {
      msgErr.className = msgErr.className.replace("show", "");
    }, 4000);
    msgErr.innerHTML = "";
    msgErr.innerHTML = "You need at least one tag for your meetup";
    tags.focus();
    return false;
  }

  if (details.value.length < 15) {
    msgErr.className = "show";
    setTimeout(() => {
      msgErr.className = msgErr.className.replace("show", "");
    }, 4000);
    msgErr.innerHTML = "";
    msgErr.innerHTML = "Details must be at least 15 characters long";
    details.focus();
    return false;
  }

  if (location.value.length < 10) {
    msgErr.className = "show";
    setTimeout(() => {
      msgErr.className = msgErr.className.replace("show", "");
    }, 4000);
    msgErr.innerHTML = "";
    msgErr.innerHTML = "location must be at least 10 characters long";
    location.focus();
    return false;
  }

  if (date.value.length < 8) {
    msgErr.className = "show";
    setTimeout(() => {
      msgErr.className = msgErr.className.replace("show", "");
    }, 4000);
    msgErr.innerHTML = "";
    msgErr.innerHTML = "date must be at least 8 characters long";
    date.focus();
    return false;
  }

  if (image.value.length > 50 || image.value.length < 5) {
    msgErr.className = "show";
    setTimeout(() => {
      msgErr.className = msgErr.className.replace("show", "");
    }, 4000);
    msgErr.innerHTML = "";
    msgErr.innerHTML = "Invalid image url. Only 5-50 characters allowed.";
    image.focus();
    return false;
  }

  post_meetup();
}

function post_meetup() {
  const form = new FormData(myForm);
  const url = "https://questioner2.herokuapp.com/api/v2/meetups";
  //   const url = "http://127.0.0.1:5000/api/v2/meetups";
  loading.className = "show";
  setTimeout(() => {
    loading.className = loading.className.replace("show", "");
  }, 15000);
  fetch(url, {
    method: "POST",
    body: form,
    headers: new Headers({
      Authorization: `Bearer ${sessionStorage.accessToken}`
    })
  })
    .then(response => response.json())
    .then(data => {
      console.log(data);
      loading.className = loading.className.replace("show", "");
      if (data.status === 201) {
        msgOk.className = "show";
        setTimeout(() => {
          msgOk.className = msgOk.className.replace("show", "");
        }, 4000);
        msgOk.innerHTML = "";
        msgOk.innerHTML = data.message;
      } else {
        msgErr.className = "show";
        setTimeout(() => {
          msgErr.className = msgErr.className.replace("show", "");
        }, 4000);
        msgErr.innerHTML = data.message;
      }
    });
}
