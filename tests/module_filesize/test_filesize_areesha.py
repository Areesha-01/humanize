import pytest
from humanize import naturalsize


@pytest.mark.order(1)
@pytest.mark.smoke
@pytest.mark.regression
def test_naturalsize_megabytes():
    assert naturalsize(1000000) == "1.0 MB"


@pytest.mark.order(1)
@pytest.mark.smoke
def test_naturalsize_kilobytes():
    assert naturalsize(1000) == "1.0 kB"


@pytest.mark.order(2)
@pytest.mark.boundary
@pytest.mark.parametrize("n, expected", [
    (0, "0 Bytes"),
    (1, "1 Byte"),
    (999, "999 Bytes"),
    (1000, "1.0 kB"),
])
def test_naturalsize_boundary(n, expected):
    assert naturalsize(n) == expected


@pytest.mark.order(3)
@pytest.mark.regression
def test_naturalsize_negative():
    assert naturalsize(-1000) == "-1.0 kB"


@pytest.mark.order(3)
@pytest.mark.regression
def test_naturalsize_binary_kib():
    assert naturalsize(1024, binary=True) == "1.0 KiB"


@pytest.mark.order(3)
@pytest.mark.regression
def test_naturalsize_binary_below_one_kib():
    assert naturalsize(1000, binary=True) == "1000 Bytes"


@pytest.mark.order(3)
@pytest.mark.regression
def test_naturalsize_gnu():
    assert naturalsize(1000, gnu=True) == "1000B"