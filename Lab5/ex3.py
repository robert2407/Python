class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def calculate_mileage(self):
        return "The average mileage for normal cars is 10 liters per 100 kilometers"

class Motorcycle(Vehicle):
    def calculate_mileage(self):
        return "The average mileage for motorcycles is 5 liters per 100 kilometers"

class Truck(Vehicle):
    def calculate_towing_capacity(self):
        return "The average towing capacity for aa truck is 10.000 NewtonMeters"


if __name__ == "__main__":
    car = Car("Honda", "Civic", 2021)
    motorcycle = Motorcycle("Honda", "CBR 600R", 2013)
    truck = Truck("Honda", "Ridgeline", 2017)

    print(car.calculate_mileage())
    print(motorcycle.calculate_mileage())
    print(truck.calculate_towing_capacity())
