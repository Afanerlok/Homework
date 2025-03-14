import pytest
import requests

BASE_URL = "https://api.openbrewerydb.org/v1/breweries"

def test_list_breweries():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.parametrize("city", ["San Diego"])
def test_breweries_by_city(city):
    response = requests.get(f"{BASE_URL}?by_city={city}")
    assert response.status_code == 200
    assert all(brewery["city"] == city for brewery in response.json())

@pytest.mark.parametrize("per_page", [1, 5, 10])
def test_breweries_per_page(per_page):
    response = requests.get(f"{BASE_URL}?per_page={per_page}")
    assert response.status_code == 200
    assert len(response.json()) == per_page

@pytest.mark.parametrize("state", ["California", "Colorado", "Oregon"])
def test_breweries_by_state(state):
    response = requests.get(f"{BASE_URL}?by_state={state}")
    assert response.status_code == 200
    assert all(brewery["state"] == state for brewery in response.json())

def test_search_breweries():
    response = requests.get(f"{BASE_URL}/search?query=dog")
    assert response.status_code == 200
    assert isinstance(response.json(), list)