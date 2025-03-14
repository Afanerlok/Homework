import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.parametrize("post_id", [1, 5, 10])
def test_get_single_post(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id

def test_create_post():
    data = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=data)
    assert response.status_code == 201
    assert response.json()["id"] == 101

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_posts_by_user(user_id):
    response = requests.get(f"{BASE_URL}/posts?userId={user_id}")
    assert response.status_code == 200
    assert all(post["userId"] == user_id for post in response.json())

def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200