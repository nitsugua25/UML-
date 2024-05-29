class TomTaGrandMere:
    def __init__(self,salope):
        self.__salope= salope
        
    def __private(self):
        a = 1 + 1 
        return a
    
    def pasPrivate(self):
        b = self.__private()
        b += 1
        return b
    
tom = TomTaGrandMere("tom")
print(tom.pasPrivate())
    