class Car:
    def __init__(self,nom,marque):
        self.__nom = nom
        self.__marque = marque
        self.__aggregation = []
        
    def addAggregation(self,element):
        self.__aggregation.append(element)
        
    def elements(self):
        for element in self.__aggregation:
            print(element)
          
    def deleteAggregation(self,element):
        self.__aggregation.remove(element)
    
    def getAggregation(self):
        return self.__aggregation
