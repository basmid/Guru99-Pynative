
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

model = Vehicle("School",180,12)
print(model.name, model.max_speed, model.mileage)
#Vehicle Name: School Volvo Speed: 180 Mileage: 12

class Bus(Vehicle):
    pass

modelBus = Bus("School",180,12)
print(modelBus.name,modelBus.max_speed,modelBus.mileage)