const meetup_info = document.getElementById("meetup");

function getMeetup() {
  const url = `https://questioner2.herokuapp.com/api/v2/meetups/${
    window.sessionStorage.m_id
  }`;
  // const url = `http://127.0.0.1:5000/api/v2/meetups/${
  //   window.sessionStorage.m_id
  // }`;
  loading.className = "show";
  setTimeout(() => {
    loading.className = loading.className.replace("show", "");
  }, 15000);
  fetch(url)
    .then(response => response.json())
    .then(data => {
      loading.className = loading.className.replace("show", "");
      if (data.status === 200) {
        let meetup = data.data[0];
        let questions = data.data;
        meetup_info.innerHTML = `<div class="grid-item main header">
            <img src="${meetup.image}" alt="meetup image" />
            <div class="text-block">
              <a href="#"><h2>${meetup.title}</h2></a>
              <small>${meetup.happening_on}</small>
              <br />
              <button class="cta-going" onclick="">I'm going!</button>
            </div>
          </div>
          
          <div class="grid-item details">
              <h3>Details</h3>
              <p>${meetup.details}</p>
              <br>
              <span><i class="fas fa-map-marker-alt"></i> ${
                meetup.location
              }</span>
              <br>
              <br>

              <h3>Any Questions?</h3>
              <div class="grid-item ask">
                  <form id="ask_form">
                      <input type="text" class="auth-input" placeholder="Question title" name="title" id="title" />
                      <textarea placeholder="Your question..." name="body" id="body"></textarea>
                      <button onclick="event.preventDefault(); validate();">Ask</button>
                  </form>
              </div>`;

        questions.forEach(({ q_title, comments }) => {
          if (q_title) {
            meetup_info.innerHTML += `<div class="flex" id="question">
                  <div class="profile">
                      <img src="http://i.pravatar.cc/300" alt="profile-image" />
                  </div>
                  <div class="question-body">
                      <p>${q_title}</p>
                        <button class="react upvote">
                            <i class='fa fa-thumbs-up'></i>
                            Upvote
                            <span id="upvotes">+1</span>
                        </button>
                        <button class="react downvote">
                            <i class='fa fa-thumbs-down'></i>
                            Downvote
                            <span id="downvotes">-1</span>
                        </button>
                        <button class="react comment" onclick="location.href = 'question/';">
                            <i class='fa fa-comment'></i>
                            Comment
                            <span id="comments">${comments}</span>
                        </button>
                  </div>
              </div>
              <div class="flex down"></div>
          </div>`;
          }
        });

        // append to the element's content
        meetup_info.innerHTML += ``;
      } else {
        msgErr.className = "show";
        setTimeout(() => {
          msgErr.className = msgErr.className.replace("show", "");
        }, 4000);
        msgErr.innerHTML = data.message;
      }
    });
}

function validate() {
  const title = document.getElementById("title");
  const body = document.getElementById("body");

  if (title.value.length < 5) {
    msgErr.className = "show";
    setTimeout(() => {
      msgErr.className = msgErr.className.replace("show", "");
    }, 4000);
    msgErr.innerHTML = "";
    msgErr.innerHTML = "Title must be at least 5 characters long";
    title.focus();
    return false;
  }

  if (body.value.length < 15) {
    msgErr.className = "show";
    setTimeout(() => {
      msgErr.className = msgErr.className.replace("show", "");
    }, 4000);
    msgErr.innerHTML = "";
    msgErr.innerHTML = "Question body must be at least 15 characters long";
    body.focus();
    return false;
  }

  postQuestion();
}

function postQuestion() {
  const myForm = document.getElementById("ask_form");
  const form = new FormData(myForm);
  const url = `https://questioner2.herokuapp.com/api/v2/meetups/${
    window.sessionStorage.m_id
  }/questions`;
  // const url = `http://127.0.0.1:5000/api/v2/meetups/${
  //   window.sessionStorage.m_id
  // }/questions`;
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