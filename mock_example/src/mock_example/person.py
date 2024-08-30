class Person: 

    def __init__(self, name, age): 
        self._name = name 
        self._age = age 

    @property 
    def name(self):
        return self._name 
    
    @property
    def age(self):
        return self._age
    
    def get_person_json(self):
        return{
            "name": self._name, 
            "age": self._age
        }