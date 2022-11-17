import pytest

from grade_upgrade import Designer, Developer


@pytest.fixture
def designer():
    def init_designer(seniority):
        return Designer(name="Vasya", seniority=seniority, awards=0)
    return init_designer

@pytest.mark.parametrize("seniority, expected", [(0, 1), (4, 1), (7, 2), (8, 2)])
def test_designer_grade(designer, seniority, expected):
    assert designer(seniority).grade == expected

@pytest.fixture
def developer():
    def init_developer(seniority):
        return Developer(name="Petr", seniority=seniority)
    return init_developer

@pytest.mark.parametrize("seniority, expected", [(0, 1), (4, 1), (5, 2), (6, 2)])
def test_developer_grade(developer, seniority, expected):
    assert developer(seniority).grade == expected
