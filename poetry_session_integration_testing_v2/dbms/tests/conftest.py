
import pytest 
from dbms import User 
from dbms import UserDatabase

@pytest.fixture(scope="module")
def user_db():
    db = UserDatabase()
    user1 = User(1, "Alice")
    user2 = User(2, "Bob")

    db.add_user(user2)
    db.add_user(user1)
    
    yield db
    del db, user1, user2