class User: 

    def __init__(self, user_id, name):
        self.id = user_id 
        self.name = name 

    
    def __eq__(self, other):
        if isinstance(other, User):
            return (self.id == other.id
                and self.name == other.name)

    def __repr__(self):
        return f"User(user_id) = {self.id}, name = {self.name}"