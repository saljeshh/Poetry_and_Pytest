from mock_example.area import area_of_circle
from unittest import mock

@mock.patch('mock_example.area.PI', 3.0)
def test_area_of_circle_with_decorator():
    assert area_of_circle(5) == 75


def test_area_of_circle_with_context_manager():
    with mock.patch('mock_example.area.PI', 3.0):
        assert area_of_circle(5) == 75

def test_area_of_circle_with_mocker(mocker):
    mocker.patch('mock_example.area.PI', 3.0)
    assert area_of_circle(5) == 75.0

def test_area_of_circle():
    radius = 5 
    expected_area = 78.5
    area = area_of_circle(radius)
    assert area == expected_area


def test_area_of_circle_with_mock_function(mocker):
    # we cant patch area_of_circle only any function inside it
    # this means in area.py.. we changed multiply and forced to return using return_value so passing in area_of_circle('hello;) will return 5
    mock_multiply = mocker.patch('mock_example.area.multiply')
    mock_multiply.return_value = 'hello'
    assert area_of_circle(5) == 'hello'