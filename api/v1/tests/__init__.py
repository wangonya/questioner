import pytest
import json
from flask_jwt_extended import create_access_token
import api

# manually push app context
# to avoid working outside of application context
ctx = api.create_app().test_request_context()
ctx.push()
access_token = create_access_token('kwangonya@gmail.com')
headers = {'Authorization': 'Bearer {}'.format(access_token)}
ctx.pop()


@pytest.fixture
def main():
    main = api.create_app()
    return main.test_client()


def post_json(main, url, json_dict):
    return main.post(url, data=json.dumps(json_dict), content_type='application/json', headers=headers)


def patch_json(main, url, json_dict):
    return main.patch(url, data=json.dumps(json_dict), content_type='application/json', headers=headers)
