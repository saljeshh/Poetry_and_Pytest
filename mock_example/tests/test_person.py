import pytest 
from mock_example.person import Person


@pytest.fixture
def person():
    return Person("Saljesh", 23)

def test_person_properties(person):
    assert person.name == 'Saljesh'
    assert person.age == 23
    assert isinstance(person.get_person_json(),dict)

def test_person_with_mock(mocker):
    person = Person('saljesh', 23)
    mocker_response = {'name': "Saljesh", 'age': 23}
    mocker.patch.object(person, "get_person_json", return_value=mocker_response)

    result = person.get_person_json()
    print(result)
    assert result == mocker_response