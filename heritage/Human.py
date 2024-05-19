class Human:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def presentation(self):
        print(f"Hello, my name is {self._name} and I am {self._age} years old.")