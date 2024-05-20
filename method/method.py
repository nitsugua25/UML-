class Method:
    def __init__(self):
        self.__value = 0
    
    # void method
    def add_one(self):
        self.__value +=1
    
    # String method
    def return_string(self):
        return "Hello World"
    
    # int method (because the value is an integer)
    def return_value(self):
        return self.__value
    
    # int method too
    def return_value_plus_one(self):
        return self.__value + 1
    
    # float method
    def return_float(self):
        return self.__value + 0.5
    
    # String too
    def return_string_and_value(self):
        return "Hello World", self.__value
    