import pytest 
from dbms import User
from dbms import UserDatabase



# pass the fixture name
def test_get_user(user_db):
    expected_user = User(1, "Alice")
    user_1 = user_db.get_user(1)
    assert user_1 == expected_user


def test_get_user_2(user_db):
    expected_user = User(2, "Bob")
    user_2 = user_db.get_user(2)
    assert user_2 == expected_user


def test_add_user(user_db):
    new_user = User(3, "Charlie")
    user_db.add_user(new_user)
    retrieved_user = user_db.get_user(3)
    print(user_db)
    assert retrieved_user == new_user