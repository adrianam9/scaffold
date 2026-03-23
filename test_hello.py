import pytest
from hello import add

@pytest.fixture
def first_value():
    return 6

@pytest.fixture
def second_value():
    return 4

def test_add(first_value,second_value):
    assert add(first_value,second_value) == 10



    
    