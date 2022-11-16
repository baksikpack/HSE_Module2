import pytest

from palindrom_checker import check_palindrome


@pytest.mark.parametrize("palindrome, expected", [("1221", True), ("1231", False), ("ротор", True), ("12332", False)])
def test_palindrome(palindrome, expected):
    assert check_palindrome(palindrome) == expected


@pytest.mark.parametrize("expected_exception, palindrome", [(TypeError, None), (TypeError, 121)])
def test_palindrome_with_error(expected_exception, palindrome):
    with pytest.raises(expected_exception):
        check_palindrome(palindrome)
