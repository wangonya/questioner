const myForm = document.getElementById("signup_form");

function validate() {
  const fname = document.getElementById("fname");
  const lname = document.getElementById("lname");
  const email = document.getElementById("email");
  const password = document.getElementById("password");

  if (fname.value.length < 4) {
    msgErr.className = "show";
    setTimeout(() => {
      msgErr.className = msgErr.className.replace("show", "");
    }, 4000);
    msgErr.innerHTML = "";
    msgErr.innerHTML = "Firstname must be at least 4 characters long";
    fname.focus();
    return false;
  }

  if (lname.value.length < 4) {
    msgErr.className = "show";
    setTimeout(() => {
      msgErr.className = msgErr.className.replace("show", "");
    }, 4000);
    msgErr.innerHTML = "";
    msgErr.innerHTML = "Lastname must be at least 4 characters long";
    lname.focus();
    return false;
  }

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

  register();
}

function register() {
  const form = new FormData(myForm);
  const url = "https://questioner2.herokuapp.com/api/v2/auth/signup";
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
      if (data.status === 201) {
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
