import pytest
from Youtube_Tutorial.Tut2.myapp.sample import validate_age

def test_validate_age():
    validate_age(12)

def test_validate_age_invalid_age():
    with pytest.raises(ValueError) as ex_info:
        validate_age(-1)
    print(str(ex_info.value))



