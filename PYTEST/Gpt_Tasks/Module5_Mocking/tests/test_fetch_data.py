from Module5_Mocking.myapp.fetch_data import fetch_weather_data
import pytest

def test_fetch_weather_data(mocker):

    mock_api_client = mocker.Mock()

    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"temperature": "20C", "condition": "Sunny"}

    mock_api_client.get.return_value = mock_response

    result = fetch_weather_data(mock_api_client)

    assert result == {"temperature": "20C", "condition": "Sunny"}
