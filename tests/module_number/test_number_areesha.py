import pytest
from humanize import intcomma, intword, ordinal


# ---------- intcomma ----------
@pytest.mark.order(1)
@pytest.mark.smoke
@pytest.mark.regression
def test_intcomma_basic():
    assert intcomma(1234567) == "1,234,567"


@pytest.mark.order(3)
@pytest.mark.regression
def test_intcomma_negative():
    assert intcomma(-1000) == "-1,000"


@pytest.mark.order(3)
@pytest.mark.regression
def test_intcomma_float():
    assert intcomma(1000.5) == "1,000.5"


@pytest.mark.order(3)
@pytest.mark.regression
def test_intcomma_invalid_string_returned_as_is():
    assert intcomma("abc") == "abc"


@pytest.mark.order(2)
@pytest.mark.boundary
@pytest.mark.parametrize("n, expected", [(0, "0"), (999, "999"), (1000, "1,000")])
def test_intcomma_boundary(n, expected):
    assert intcomma(n) == expected


# ---------- intword ----------
@pytest.mark.order(1)
@pytest.mark.smoke
@pytest.mark.regression
def test_intword_millions():
    assert intword(1200000) == "1.2 million"


@pytest.mark.order(3)
@pytest.mark.regression
def test_intword_negative():
    assert intword(-1500000) == "-1.5 million"


@pytest.mark.order(3)
@pytest.mark.regression
def test_intword_invalid_string():
    assert intword("abc") == "abc"


@pytest.mark.order(2)
@pytest.mark.boundary
@pytest.mark.parametrize("n, expected", [
    (999, "999"),
    (1000, "1.0 thousand"),
    (1000000, "1.0 million"),
    (1000000000, "1.0 billion"),
])
def test_intword_boundary(n, expected):
    assert intword(n) == expected


# ---------- ordinal ----------
@pytest.mark.order(1)
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("n, expected", [
    (1, "1st"), (2, "2nd"), (3, "3rd"), (4, "4th"),
    (21, "21st"), (22, "22nd"), (23, "23rd"), (101, "101st"),
])
def test_ordinal_suffixes(n, expected):
    assert ordinal(n) == expected


@pytest.mark.order(2)
@pytest.mark.boundary
@pytest.mark.parametrize("n, expected", [(11, "11th"), (12, "12th"), (13, "13th"), (111, "111th")])
def test_ordinal_teens_exception(n, expected):
    assert ordinal(n) == expected


@pytest.mark.order(2)
@pytest.mark.boundary
def test_ordinal_zero():
    assert ordinal(0) == "0th"


@pytest.mark.order(3)
@pytest.mark.regression
def test_ordinal_invalid_string():
    assert ordinal("abc") == "abc"