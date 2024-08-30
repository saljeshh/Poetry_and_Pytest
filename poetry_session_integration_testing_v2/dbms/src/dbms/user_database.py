class UserDatabase:
    def __init__(self):
        self.users = {}

    
    def add_user(self, user):
        self.users[user.id] = user 

    def get_user(self, user_id):
        return self.users.get(user_id)
    
    def __repr__(self):
        return f"UserDatabase(users = {self.users})"