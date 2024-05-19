class Method:
    def __init__(self):
        self.__value = 0
    
    # void method
    def add_one(self):
        self.__value +=1
    
    def return_string(self):
        return "Hello World"
    
    def return_value(self):
        return self.__value
    
    def return_value_plus_one(self):
        return self.__value + 1
    
    def return_float(self):
        return self.__value + 0.5
    
    def return_string_and_value(self):
        return "Hello World", self.__value
    