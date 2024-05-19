class Engine:
    def __init__(self, power = False):
        self.__power = power

    def start(self):
        self.__power = True
        
    def stop(self):
        self.__power = False