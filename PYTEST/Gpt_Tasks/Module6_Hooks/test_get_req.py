import pytest

@pytest.mark.parametrize(
    "endpoint, expected",
    [
        ("/posts",100),
        ("/comments",500),
        ("/albums",100),
        ("/photos",5000),
        ("/todos",200),
        ("/users",10)
    ]
)
def test_get_req(api_client, endpoint, expected):
    response = api_client.get_req(endpoint)

    assert response.status_code == 200
    data = response.json()
    assert len(data) == expected
