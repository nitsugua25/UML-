class Car:
    def __init__(self, name):
        self.__name = name
        self.__composition = []
        
    def addComposition(self, element):
        self.__composition.append(element)
    
    def show_elements(self):
        for element in self.__composition:
            print(element)
            
    def getComposition(self):
        return self.__composition
    
    def deleteComposition(self, element):
        self.__composition.remove(element)