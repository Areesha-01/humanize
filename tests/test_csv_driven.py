import csv
from pathlib import Path

import pytest
from humanize import intcomma, intword, naturalsize, ordinal

CSV_FILE = Path(__file__).parent / "data" / "test_data.csv"

FUNCTIONS = {
    "intcomma": intcomma,
    "intword": intword,
    "ordinal": ordinal,
    "naturalsize": naturalsize,
}


def load_csv_cases():
    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        return [(r["function"], int(r["input"]), r["expected"]) for r in csv.DictReader(f)]


@pytest.mark.order(2)
@pytest.mark.regression
@pytest.mark.parametrize("func_name, value, expected", load_csv_cases())
def test_from_csv(func_name, value, expected):
    assert FUNCTIONS[func_name](value) == expected