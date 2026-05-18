import pytest
from mocking_tut.Source import services
import unittest.mock as mock

@mock.patch("Mocking.Source.services.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):

    mock_get_user_from_db.return_value = 'Mocked_pranav'
    user_id = services.get_user_from_db(1)

    assert user_id == 'Mocked_pranav'
