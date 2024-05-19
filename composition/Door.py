class Door:
    def __init__(self):
        self.__isOpen = False

    def open(self):
        self.__isOpen = True

    def close(self):
        self.__isOpen = False
    
    def __str__(self):
        return "Door is open" if self.__isOpen else "Door is closed"
    