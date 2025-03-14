import pytest
import requests

BASE_URL = "https://dog.ceo/api"

def test_list_all_breeds():
    response = requests.get(f"{BASE_URL}/breeds/list/all")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "status" in response.json()
    assert isinstance(response.json()["message"], dict)

@pytest.mark.parametrize("breed", ["hound", "bulldog", "poodle"])
def test_random_image_by_breed(breed):
    response = requests.get(f"{BASE_URL}/breed/{breed}/images/random")
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"].endswith(".jpg")

def test_multiple_random_images():
    response = requests.get(f"{BASE_URL}/breeds/image/random/3")
    assert response.status_code == 200
    assert len(response.json()["message"]) == 3

def test_sub_breeds():
    response = requests.get(f"{BASE_URL}/breed/hound/list")
    assert response.status_code == 200
    assert isinstance(response.json()["message"], list)

@pytest.mark.parametrize("count", [1, 5, 10])
def test_random_images(count):
    response = requests.get(f"{BASE_URL}/breeds/image/random/{count}")
    assert response.status_code == 200
    assert len(response.json()["message"]) == count