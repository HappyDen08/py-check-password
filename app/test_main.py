import pytest
from app.main import check_password


@pytest.mark.parametrize("password, valid",
                         [
                             ("Pass@word1", True),
                             ("qwerty", False),
                             ("qwertyuiopasdfghjkl", False),
                             ("asdqwd", False)
                         ])
def test_our_funk(password: str, valid: bool) -> None:
    assert check_password(password) == valid
