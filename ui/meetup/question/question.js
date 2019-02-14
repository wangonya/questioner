const q_top = document.getElementById("main_q");

function getQuestion() {
  const url = `https://questioner2.herokuapp.com/api/v2/questions/${
    window.sessionStorage.q_id
  }`;
  //   const url = `http://127.0.0.1:5000/api/v2/questions/${
  //     window.sessionStorage.q_id
  //   }`;
  loading.className = "show";
  setTimeout(() => {
    loading.className = loading.className.replace("show", "");
  }, 15000);
  fetch(url)
    .then(response => response.json())
    .then(data => {
      loading.className = loading.className.replace("show", "");
      if (data.status === 200) {
        let question = data.data[0];
        let answers = data.data;
        q_top.innerHTML = ` <div class="flex" id="question">
                <div class="profile">
                    <img src="http://i.pravatar.cc/300" alt="author" />
                    <small id="author">Jane</small>
                </div>
                <div class="question-body">
                    <h3>${question.title}</h3>
                    <p>${question.body}</p>
                    <button class="react upvote" onclick="upvote(${
                      window.sessionStorage.q_id
                    })">
                            <i class='fa fa-thumbs-up'></i>
                            Upvote
                            <span id="upvotes">+1</span>
                        </button>
                        <button class="react downvote" onclick="downvote(${
                          window.sessionStorage.q_id
                        })">
                            <i class='fa fa-thumbs-down'></i>
                            Downvote
                            <span id="downvotes">-1</span>
                        </button>
                </div>
            </div><div id="comment-count">${answers.length} comments</div>`;

        answers.forEach(({ q_comment }) => {
          q_top.innerHTML += `
            <div class="flex" id="answer">
                <div class="profile">
                    <img src="http://i.pravatar.cc/300" alt="author" />
                    <small id="author">Mercy</small>
                </div>
                <div class="answer-body">
                    <p>${q_comment}</p>
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

function validate() {
  const body = document.getElementById("answer_body");

  if (body.value.length < 15) {
    msgErr.className = "show";
    setTimeout(() => {
      msgErr.className = msgErr.className.replace("show", "");
    }, 4000);
    msgErr.innerHTML = "";
    msgErr.innerHTML = "Answer body must be at least 15 characters long";
    body.focus();
    return false;
  }

  postQuestion();
}

function postQuestion() {
  const myForm = document.getElementById("answer_form");
  const form = new FormData(myForm);
  const url = `https://questioner2.herokuapp.com/api/v2/comments/${
    window.sessionStorage.q_id
  }`;
  //   const url = `http://127.0.0.1:5000/api/v2/comments/${
  //     window.sessionStorage.q_id
  //   }`;
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
        q_top.innerHTML = "";
        document.getElementById("answer_body").value = "";
        getQuestion();
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
  const url = `https://questioner2.herokuapp.com/api/v2/questions/${id}/upvote`;
  // const url = `http://127.0.0.1:5000/api/v2/questions/${id}/upvote`;
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
}

function downvote(id) {
  const url = `https://questioner2.herokuapp.com/api/v2/questions/${id}/downvote`;
  // const url = `http://127.0.0.1:5000/api/v2/questions/${id}/downvote`;
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
}
