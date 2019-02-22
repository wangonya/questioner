const meetup_info = document.getElementById("meetup");

function getMeetup() {
  const url = `https://questioner2.herokuapp.com/api/v2/meetups/${
    window.sessionStorage.m_id
  }`;
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
              <br />
              <h3>Going?
                <button class="react yes" onclick="rsvp(${meetup.id}, 'yes')">
                  <i class="far fa-smile fa-2x"></i>
                  <span>Yes</span>
              </button>
              <button class="react maybe" onclick="rsvp(${meetup.id}, 'maybe')">
                  <i class="far fa-meh fa-2x"></i>
                  <span>Maybe</span>
              </button>
              <button class="react no" onclick="rsvp(${meetup.id}, 'no')">
                  <i class="far fa-frown fa-2x"></i>
                  <span>No</span>
              </button>
              </h3>
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

        questions.forEach(({ q_title, comments, q_id }) => {
          if (q_title) {
            meetup_info.innerHTML += `<div class="flex" id="question">
                  <div class="profile">
                      <img src="http://i.pravatar.cc/300" alt="profile-image" />
                  </div>
                  <div class="question-body">
                      <p onclick="goToSpecificQuestion(${q_id})">${q_title}</p>
                        <button class="react upvote" onclick="upvote(${q_id})">
                            <i class='fa fa-thumbs-up'></i>
                            Upvote
                            <span id="upvotes">+1</span>
                        </button>
                        <button class="react downvote" onclick="downvote(${q_id})">
                            <i class='fa fa-thumbs-down'></i>
                            Downvote
                            <span id="downvotes">-1</span>
                        </button>
                        <button class="react comment" onclick="goToSpecificQuestion(${q_id})">
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

  if (sessionStorage.accessToken) {
    postQuestion();
  } else {
    msgErr.className = "show";
    setTimeout(() => {
      msgErr.className = msgErr.className.replace("show", "");
    }, 4000);
    msgErr.innerHTML = "Plese log in to post question";
  }
}

function postQuestion() {
  const myForm = document.getElementById("ask_form");
  const form = new FormData(myForm);
  const url = `https://questioner2.herokuapp.com/api/v2/meetups/${
    window.sessionStorage.m_id
  }/questions`;
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
        meetup_info.value = "";
        getMeetup();
      } else {
        msgErr.className = "show";
        setTimeout(() => {
          msgErr.className = msgErr.className.replace("show", "");
        }, 4000);
        msgErr.innerHTML = data.message;
      }
    });
}

function upvote(id) {
  if (sessionStorage.accessToken) {
    const url = `https://questioner2.herokuapp.com/api/v2/questions/${id}/upvote`;
    loading.className = "show";
    setTimeout(() => {
      loading.className = loading.className.replace("show", "");
    }, 15000);
    fetch(url, {
      method: "PATCH",
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
  } else {
    msgErr.className = "show";
    setTimeout(() => {
      msgErr.className = msgErr.className.replace("show", "");
    }, 4000);
    msgErr.innerHTML = "Plese log in to vote";
  }
}

function downvote(id) {
  if (sessionStorage.accessToken) {
    const url = `https://questioner2.herokuapp.com/api/v2/questions/${id}/downvote`;
    loading.className = "show";
    setTimeout(() => {
      loading.className = loading.className.replace("show", "");
    }, 15000);
    fetch(url, {
      method: "PATCH",
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
  } else {
    msgErr.className = "show";
    setTimeout(() => {
      msgErr.className = msgErr.className.replace("show", "");
    }, 4000);
    msgErr.innerHTML = "Plese log in to vote";
  }
}

function rsvp(id, res) {
  if (sessionStorage.accessToken) {
    const url = `https://questioner2.herokuapp.com/api/v2/meetups/${id}/rsvps`;
    loading.className = "show";
    setTimeout(() => {
      loading.className = loading.className.replace("show", "");
    }, 15000);
    fetch(url, {
      method: "POST",
      body: JSON.stringify({ status: res }),
      headers: new Headers({
        Authorization: `Bearer ${sessionStorage.accessToken}`,
        "Content-Type": "application/json"
      })
    })
      .then(response => response.json())
      .then(data => {
        loading.className = loading.className.replace("show", "");
        if (data.status === 201 || 200) {
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
  } else {
    msgErr.className = "show";
    setTimeout(() => {
      msgErr.className = msgErr.className.replace("show", "");
    }, 4000);
    msgErr.innerHTML = "Plese log in to rsvp";
  }
}

function goToSpecificQuestion(id) {
  window.location.replace("question/");
  window.sessionStorage.q_id = id;
}
