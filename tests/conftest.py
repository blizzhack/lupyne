import csv
import itertools
import os
import shutil
import tempfile
from datetime import datetime
import pytest
import lucene
from lupyne import engine

dirname = os.path.join(os.path.dirname(__file__), 'fixtures')


def pytest_report_header(config):
    return 'PyLucene ' + lucene.VERSION


def pytest_configure(config):
    assert lucene.initVM(vmargs='-Djava.awt.headless=true')


@pytest.fixture
def tempdir():
    tempdir = tempfile.mkdtemp(dir=dirname)
    yield tempdir
    shutil.rmtree(tempdir)


def fixture(gen):
    return pytest.fixture(lambda: gen())


@fixture
def fields():
    yield engine.Field.Text('text', storeTermVectors=True, storeTermVectorPositions=True, storeTermVectorOffsets=True)
    for name in ('article', 'amendment', 'date'):
        yield engine.Field.String(name, stored=True)


@fixture
def constitution():
    lines = open(os.path.join(dirname, 'constitution.txt'))
    items = itertools.groupby(lines, lambda l: l.startswith('Article ') or l.startswith('Amendment '))
    for _, (header,) in items:
        _, lines = next(items)
        header, num = header.rstrip('.\n').split(None, 1)
        fields = {header.lower(): num, 'text': ''.join(lines)}
        if header == 'Amendment':
            num, date = num.split()
            date = datetime.strptime(date, '%m/%d/%Y').date()
            fields.update({header.lower(): num, 'date': str(date)})
        yield fields


@fixture
def zipcodes():
    lines = open(os.path.join(dirname, 'zipcodes.txt'))
    for zipcode, latitude, longitude, state, city, county in csv.reader(lines):
        yield {
            'zipcode': zipcode,
            'latitude': float(latitude),
            'longitude': float(longitude),
            'city': city.title(),
            'county': county.title(),
            'state': state,
        }
