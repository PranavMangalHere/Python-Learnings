import pytest
import requests

from Module5_Mocking.myapp import ex1
import unittest.mock as mock

@mock.patch("Module5_Mocking.myapp.ex1.get_user_from_db")
def test_mock_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked_Pranav"
    user_id = ex1.get_user_from_db(1)
    assert user_id == "Mocked_Pranav"

@mock.patch("requests.get")
def test_get_user(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": "ewrdf"}
    mock_get.return_value = mock_response
    data = ex1.get_user()
    assert data == {"id": "ewrdf"}

@mock.patch("requests.get")
def test_get_user_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.exceptions.HTTPError):
        ex1.get_user()