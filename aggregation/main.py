from Car import Car
from Engine import Engine
from Door import Door

if __name__ == "__main__":
    car = Car("Jazz","Honda")
    engine = Engine()
    door = Door()
    car.addAggregation(engine)
    car.addAggregation(door)
    car.elements()
    print(car.getAggregation())