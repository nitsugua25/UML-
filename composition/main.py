from Car import Car
from Engine import Engine
from Door import Door

if __name__ == "__main__":
    car = Car("Jazz","Honda")
    engine = Engine()
    door = Door()
    car.add_composition(engine)
    car.add_composition(door)
    car.elements()