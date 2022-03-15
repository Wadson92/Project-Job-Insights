from src.sorting import sort_by
import pytest


MOCK_JOBS = [
    {"max_salary": 0, "min_salary": 10, "date_posted": "2020-04-20"},
    {"max_salary": 1500, "min_salary": 0, "date_posted": "2020-04-24"},
    {"max_salary": 10, "min_salary": 100, "date_posted": "2020-04-21"},
    {"max_salary": 10000, "min_salary": 200, "date_posted": "2020-04-22"},
    {"max_salary": 15000, "min_salary": 4, "date_posted": "2020-04-23"},
]

MOCK_JOBS_MIN = [
    {"max_salary": 1500, "min_salary": 0, "date_posted": "2020-04-24"},
    {"max_salary": 15000, "min_salary": 4, "date_posted": "2020-04-23"},
    {"max_salary": 0, "min_salary": 10, "date_posted": "2020-04-20"},
    {"max_salary": 10, "min_salary": 100, "date_posted": "2020-04-21"},
    {"max_salary": 10000, "min_salary": 200, "date_posted": "2020-04-22"},
]


MOCK_JOBS_MAX = [
    {"max_salary": 15000, "min_salary": 4, "date_posted": "2020-04-23"},
    {"max_salary": 10000, "min_salary": 200, "date_posted": "2020-04-22"},
    {"max_salary": 1500, "min_salary": 0, "date_posted": "2020-04-24"},
    {"max_salary": 10, "min_salary": 100, "date_posted": "2020-04-21"},
    {"max_salary": 0, "min_salary": 10, "date_posted": "2020-04-20"},
]


MOCK_JOBS_DATE = [
    {"max_salary": 1500, "min_salary": 0, "date_posted": "2020-04-24"},
    {"max_salary": 15000, "min_salary": 4, "date_posted": "2020-04-23"},
    {"max_salary": 10000, "min_salary": 200, "date_posted": "2020-04-22"},
    {"max_salary": 10, "min_salary": 100, "date_posted": "2020-04-21"},
    {"max_salary": 0, "min_salary": 10, "date_posted": "2020-04-20"},
]


def test_sort_by_criteria():
    sort_by(MOCK_JOBS, 'min_salary')
    assert MOCK_JOBS == MOCK_JOBS_MIN
    sort_by(MOCK_JOBS, 'max_salary')
    assert MOCK_JOBS == MOCK_JOBS_MAX
    sort_by(MOCK_JOBS, 'date_posted')
    assert MOCK_JOBS == MOCK_JOBS_DATE
    with pytest.raises(ValueError, match="invalid sorting criteria: min"):
        assert sort_by(MOCK_JOBS, 'min')
