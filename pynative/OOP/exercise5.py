

class Vehicle:
    a = "I am a class attribute"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
# Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18

auto = Vehicle("Opel",230,18)
print(auto.a)
auto2 = Bus("Volvo",220,19)
print(auto2.a)