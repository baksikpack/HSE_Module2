import pytest
import requests
from rate import Rate


class MockResponse:

    @staticmethod
    def json():
        return {
                "Valute":
                    {
                    "USD":
                        {
                        "ID": "R01235",
                        "NumCode": "840",
                        "CharCode": "USD",
                        "Nominal": 1,
                        "Name": "Доллар США",
                        "Value": 61.1629,
                        "Previous": 61.1958
                        }
                    }
                }


@pytest.fixture
def mock_response(monkeypatch):

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    # init_rate = Rate()
    # assert init_rate.make_format("USD") == 61.1629


@pytest.fixture
def rate(mock_response):

    def init_rate(format_, diff):
        return Rate(format_=format_, diff=diff)

    return init_rate


@pytest.mark.parametrize("format_, diff, expected", [("Value", "False", 61.1629),
                                                     ("Value", "True", -0.03289999999999793), #проблема понятна, пока оставлю так и ушел в гугл
                                                     ("Full", "False", {
                                                                         "ID": "R01235",
                                                                         "NumCode": "840",
                                                                         "CharCode": "USD",
                                                                         "Nominal": 1,
                                                                         "Name": "Доллар США",
                                                                         "Value": 61.1629,
                                                                         "Previous": 61.1958
                                                                                           }),
                                                     ("Full", "True", {
                                                                     "ID": "R01235",
                                                                     "NumCode": "840",
                                                                     "CharCode": "USD",
                                                                     "Nominal": 1,
                                                                     "Name": "Доллар США",
                                                                     "Value": 61.1629,
                                                                     "Previous": 61.1958
                                                                                        })])


def test_make_format(rate, format_, diff, expected):
    assert rate(format_, diff).make_format("USD") == expected
