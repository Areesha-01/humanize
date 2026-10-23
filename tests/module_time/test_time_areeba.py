import datetime as dt

import pytest
from humanize import naturaldelta, naturaltime

T = dt.timedelta


# ---------- naturaldelta ----------
@pytest.mark.order(1)
@pytest.mark.smoke
@pytest.mark.regression
def test_naturaldelta_two_hours():
    assert naturaldelta(T(hours=2)) == "2 hours"


@pytest.mark.order(1)
@pytest.mark.smoke
def test_naturaldelta_thirty_seconds():
    assert naturaldelta(T(seconds=30)) == "30 seconds"


@pytest.mark.order(2)
@pytest.mark.boundary
@pytest.mark.parametrize("seconds, expected", [
    (0, "a moment"),
    (1, "a second"),
    (59, "59 seconds"),
    (60, "a minute"),
    (3600, "an hour"),
    (86400, "a day"),
])
def test_naturaldelta_boundary(seconds, expected):
    assert naturaldelta(T(seconds=seconds)) == expected


@pytest.mark.order(3)
@pytest.mark.regression
def test_naturaldelta_days_and_years():
    assert naturaldelta(T(days=2)) == "2 days"
    assert naturaldelta(T(days=365)) == "a year"


@pytest.mark.order(3)
@pytest.mark.regression
def test_naturaldelta_negative_uses_absolute_value():
    assert naturaldelta(T(seconds=-120)) == "2 minutes"


@pytest.mark.order(3)
@pytest.mark.regression
def test_naturaldelta_accepts_plain_seconds():
    assert naturaldelta(45) == "45 seconds"


@pytest.mark.order(3)
@pytest.mark.regression
def test_naturaldelta_invalid_string_returned_as_is():
    assert naturaldelta("abc") == "abc"


@pytest.mark.order(3)
@pytest.mark.regression
def test_naturaldelta_minimum_unit_milliseconds():
    assert naturaldelta(T(milliseconds=500), minimum_unit="milliseconds") == "500 milliseconds"


# ---------- naturaltime ----------
@pytest.mark.order(1)
@pytest.mark.smoke
@pytest.mark.regression
def test_naturaltime_past():
    assert naturaltime(T(seconds=30)) == "30 seconds ago"


@pytest.mark.order(1)
@pytest.mark.smoke
def test_naturaltime_future():
    assert naturaltime(T(seconds=-30)) == "30 seconds from now"


@pytest.mark.order(2)
@pytest.mark.boundary
def test_naturaltime_zero_is_now():
    assert naturaltime(T(seconds=0)) == "now"


@pytest.mark.order(2)
@pytest.mark.boundary
@pytest.mark.parametrize("seconds, past, future", [
    (1, "a second ago", "a second from now"),
    (60, "a minute ago", "a minute from now"),
    (3600, "an hour ago", "an hour from now"),
    (86400, "a day ago", "a day from now"),
])
def test_naturaltime_boundary(seconds, past, future):
    assert naturaltime(T(seconds=seconds)) == past
    assert naturaltime(T(seconds=-seconds)) == future


@pytest.mark.order(3)
@pytest.mark.regression
def test_naturaltime_datetime_with_when_past():
    value = dt.datetime(2020, 1, 1, 12, 0, 0)
    now = dt.datetime(2020, 1, 1, 12, 5, 0)
    assert naturaltime(value, when=now) == "5 minutes ago"


@pytest.mark.order(3)
@pytest.mark.regression
def test_naturaltime_datetime_with_when_future():
    value = dt.datetime(2020, 1, 1, 12, 10, 0)
    now = dt.datetime(2020, 1, 1, 12, 5, 0)
    assert naturaltime(value, when=now) == "5 minutes from now"


@pytest.mark.order(3)
@pytest.mark.regression
def test_naturaltime_invalid_string_returned_as_is():
    assert naturaltime("abc") == "abc"
