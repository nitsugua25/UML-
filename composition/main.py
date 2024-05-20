from Car import Car
from Engine import Engine
from Door import Door

if __name__ == "__main__":
    car = Car("Jazz")
    
    car.addComposition(Engine())
    car.addComposition(Door())
    car.show_elements()
    print(car.getComposition())