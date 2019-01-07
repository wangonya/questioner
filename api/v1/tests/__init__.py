import pytest
import json
import v1


@pytest.fixture
def main():
    main = v1.create_app()
    return main.test_client()


def post_json(main, url, json_dict):
    return main.post(url, data=json.dumps(json_dict), content_type='application/json', headers='')


def patch_json(main, url, json_dict):
    return main.patch(url, data=json.dumps(json_dict), content_type='application/json', headers='')
