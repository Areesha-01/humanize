# SQE Assignment 3: Unit Test Automation (humanize)

**Project:** [humanize](https://github.com/python-humanize/humanize), an open-source Python library
**Group:** Areesha (Areesha-01), Areeba (areebagujj)

## Setup video
https://drive.google.com/file/d/1Me4pHJ4wZWx1LoYSXtMm2ZOikfUdP9ih/view?usp=drive_link

(The video is hosted on Google Drive because it is larger than GitHub's 100 MB file limit.)

## Setup
```bash
git clone https://github.com/Areesha-01/humanize.git
cd humanize
python -m venv venv
venv\Scripts\activate
pip install -e .
pip install -r requirements.txt
```

## Modules tested
1. `humanize.number` (intcomma, intword, ordinal)
2. `humanize.filesize` (naturalsize)
3. `humanize.time` (naturaldelta, naturaltime)

Test design notes (ECP and BVA): `docs/test_design.md`

## How to run
```bash
pytest -v                      # all tests
pytest -m smoke                # smoke group
pytest -m boundary             # boundary value tests
pytest -m regression           # regression group
pytest -n auto                 # parallel run (pytest-xdist)
pytest --cov=humanize --cov-report=html --html=report.html --self-contained-html
```

## Execution order
Handled by pytest-order: smoke tests run first (order 1), boundary tests next (order 2), regression tests last (order 3).

## Test data
CSV-driven tests read `tests/data/test_data.csv` (see `tests/test_csv_driven.py`).

---