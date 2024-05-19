class Car:
    def __init__(self,nom,marque):
        self.__nom = nom
        self.__marque = marque
        self.__compostion = []
        
    def add_composition(self,element):
        self.__compostion.append(element)
        
    def elements(self):
        for i in self.__compostion:
            print(i)
    
    def element_precis(self):
        for element in self.__compostion:
            print(element)
          
    def delete_composition(self,element):
        self.__compostion.remove(element)
    
    def get_composition(self):
        return self.__compostion
