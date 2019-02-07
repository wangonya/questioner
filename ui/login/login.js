const myForm = document.getElementById("login_form");

function validate() {
  const email = document.getElementById("email");
  const password = document.getElementById("password");

  if (email.value.length < 4) {
    msgErr.className = "show";
    setTimeout(() => {
      msgErr.className = msgErr.className.replace("show", "");
    }, 4000);
    msgErr.innerHTML = "";
    msgErr.innerHTML = "Email must be at least 4 characters long";
    email.focus();
    return false;
  } else if (
    /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(myForm.email.value) ==
    false
  ) {
    msgErr.className = "show";
    setTimeout(() => {
      msgErr.className = msgErr.className.replace("show", "");
    }, 4000);
    msgErr.innerHTML = "";
    msgErr.innerHTML = "Invalid email format";
    lname.focus();
    return false;
  }

  if (password.value.length < 6) {
    msgErr.className = "show";
    setTimeout(() => {
      msgErr.className = msgErr.className.replace("show", "");
    }, 4000);
    msgErr.innerHTML = "";
    msgErr.innerHTML = "Password must be at least 6 characters long";
    password.focus();
    return false;
  }

  login();
}

function login() {
  const form = new FormData(myForm);
  const url = "https://questioner2.herokuapp.com/api/v2/auth/login";
  // const url = "http://127.0.0.1:5000/api/v2/auth/login";
  loading.className = "show";
  setTimeout(() => {
    loading.className = loading.className.replace("show", "");
  }, 15000);
  fetch(url, {
    method: "POST",
    body: form
  })
    .then(response => response.json())
    .then(data => {
      loading.className = loading.className.replace("show", "");
      if (data.status === 200) {
        window.location.replace("../profile");
        window.sessionStorage.accessToken = data.data[0].access_token;
      } else {
        msgErr.className = "show";
        setTimeout(() => {
          msgErr.className = msgErr.className.replace("show", "");
        }, 4000);
        msgErr.innerHTML = data.message;
      }
    });
}
