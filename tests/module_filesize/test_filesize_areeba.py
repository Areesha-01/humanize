import pytest
from humanize import naturalsize


@pytest.mark.order(1)
@pytest.mark.smoke
@pytest.mark.regression
def test_naturalsize_gigabytes():
    assert naturalsize(1000000000) == "1.0 GB"


@pytest.mark.order(2)
@pytest.mark.boundary
@pytest.mark.parametrize("n, expected", [
    (1000000, "1.0 MB"),
    (1000000000, "1.0 GB"),
    (1000000000000, "1.0 TB"),
    (1000000000000000, "1.0 PB"),
])
def test_naturalsize_unit_boundaries(n, expected):
    assert naturalsize(n) == expected


@pytest.mark.order(3)
@pytest.mark.regression
def test_naturalsize_rounding():
    assert naturalsize(1234567890) == "1.2 GB"


@pytest.mark.order(3)
@pytest.mark.regression
def test_naturalsize_float_input():
    assert naturalsize(1536.5) == "1.5 kB"


@pytest.mark.order(3)
@pytest.mark.regression
def test_naturalsize_numeric_string_input():
    assert naturalsize("2000") == "2.0 kB"


@pytest.mark.order(3)
@pytest.mark.regression
def test_naturalsize_custom_format():
    assert naturalsize(1500, format="%.3f") == "1.500 kB"


@pytest.mark.order(3)
@pytest.mark.regression
def test_naturalsize_invalid_string_raises_valueerror():
    with pytest.raises(ValueError):
        naturalsize("abc")


@pytest.mark.order(3)
@pytest.mark.regression
@pytest.mark.parametrize("n, expected", [(1000000000, "953.7 MiB"), (1000000000000, "931.3 GiB")])
def test_naturalsize_binary_large_values(n, expected):
    assert naturalsize(n, binary=True) == expected


@pytest.mark.order(3)
@pytest.mark.regression
@pytest.mark.parametrize("n, expected", [(1024, "1.0K"), (1536, "1.5K")])
def test_naturalsize_gnu_style(n, expected):
    assert naturalsize(n, gnu=True) == expected
