from Basic_operations.get_req import APIClient
import pytest

# def test_get_post():
#
#     response = get_post(1)
#
#     assert  response.status_code == 200

def test_get_req(api_client):
    response = api_client.get_req("/posts")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert "id" in data[0]

def test_post_req(api_client):
    response = api_client.post_req("/posts")
    assert response.status_code == 201

def test_put_req(api_client):
    response = api_client.put_req("/posts/1")
    assert response.status_code == 200

def test_def_req(api_client):
    response = api_client.del_req("/posts/1")
    assert response.status_code == 200

def test_get_specific_user(api_client):
    response = api_client.get_specific_user("/posts/1/comments")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert "id" in data[0]

