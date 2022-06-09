import json
import requests
import pytest

with open("data.json", "r") as f:
    data = json.load(f)

user_data = {
    "username": "Evgenii",
    "email": "eskrasnov7000@gmail.com",
    "group": []
}
update_user = {
    "username": "Eugene",
    "email": "eskrasnov.1@gmail.com"
}

user_login = data['users']['user_admin']
password = data['users']['pass_admin']


def get_existed_emails(response):
    users_email = []
    for user in response['results']:
        users_email.append(user['email'])
    return users_email


def test_create_user():
    url = f"{data['urls']['base_url']}{data['urls']['users']}"
    resp_get = requests.get(url, auth=(user_login, password))
    assert resp_get.status_code == 200
    if user_data['email'] not in get_existed_emails(resp_get.json()):
        resp_post = requests.post(url, user_data, auth=(user_login, password))
        pytest.user_id = resp_post.json()['url'].split('/', maxsplit=4)[4]
        assert resp_post.status_code == 201
    else:
        print(f"User with email {user_data['email']} exist")


def test_read_user():
    url = f"{data['urls']['base_url']}{data['urls']['users']}" \
          f"{pytest.user_id}"
    resp_get = requests.get(url, auth=(user_login, password))
    assert resp_get.status_code == 200
    assert resp_get.json()['email'] == user_data['email']


def test_update_user():
    url = f"{data['urls']['base_url']}{data['urls']['users']}" \
          f"{pytest.user_id}"
    resp_put = requests.put(url, update_user, auth=(user_login, password))
    assert resp_put.status_code == 200
    assert resp_put.json()['email'] == update_user['email']

def test_delete_user():
    url = f"{data['urls']['base_url']}{data['urls']['users']}" \
          f"{pytest.user_id}"
    resp_delete = requests.delete(url, auth=(user_login, password))
    assert resp_delete.status_code == 204
