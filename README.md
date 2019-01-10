# questioner
[![Build Status](https://travis-ci.org/wangonya/questioner.svg?branch=develop)](https://travis-ci.org/wangonya/questioner)
[![Coverage Status](https://coveralls.io/repos/github/wangonya/questioner/badge.svg?branch=bg-fix-travis-163085391)](https://coveralls.io/github/wangonya/questioner?branch=bg-fix-travis-163085391)

Crowd-source questions for a meetup. Questioner helps the meetup organizer prioritize questions to be answered. Other users can vote on asked questions and they bubble to the top or bottom of the log.

# Api endpoints
|Endpoint  |Functionality   |Route   |
|---|---|---|
|POST /signup   |Register new user   |/api/v1/auth/signup   |
|POST /login   |Login registered user   |/api/v1/auth/login   |
|POST /reset   |Reset password   |/api/v1/auth/reset   |
|POST /meetups*   |Create new meetup   |/api/v1/meetups   |
|GET /meetups/< meetup-id >   |Fetch specific meetup record   |/api/v1/meetups/< meetup-id >   |
|GET /meetups/upcoming   |Get all upcoming meetups   |/api/v1/meetups/upcoming   |
|POST /questions   |Post a new question on a meetup   |/api/v1//questions   |
|PATCH /questions/< question-id >/upvote   |Upvote a specific question   |/api/v1/questions/< question-id >/upvote   |
|PATCH /questions/< question-id >/downvote   |Downvote a specific question   |/api/v1/questions/< question-id >/downvote   |
|POST /meetups/< meetup-id >/rsvps   |Respond to meetup RSVP   |/api/v1/meetups/< meetup-id >/rsvps   |

**Endpoints marked with * are only accessible to admin users**

# How to run the app
* Clone the repo
* Activate venv and run `pip3 install requirements.txt`
* Run `run.py`
* Use a Rest client to test the endpoints

# Running tests
* Pytest is used as the test client. In the project directory, run: `pytest -vv` to run the tests, or `pytest -cov=/app` to see the coverage