import pytest


@pytest.fixture(scope='session')
def config():
    return {'sources': [
        {'url': 'http;//example.com'},
        {'url': 'http;//example.com'},
        {'url': 'http;//aaa.com'}
    ]}
