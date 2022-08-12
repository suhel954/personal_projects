# #Vehicle Name: School Volvo Speed: 180 Mileage: 12
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def seating_capacity(self, capacity):
#         return f"The capacity of {self.name} is {capacity} passengers"
#
# class Bus(Vehicle):
#     def seating_capacity(self, capacity= 50):
#         return super().seating_capacity(capacity=50)
#
#
# bus1 = Bus('School Volvo', 180, 12)
#
# print(bus1.seating_capacity())


class Vehicle:
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def description(self):
        return 'Color: {}, Vehicle name: {}, Speed: {}, Mileage: {}'.format(self.color, self.name, self.max_speed, self.mileage)

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

bus1 = Bus('School Volvo', 180, 12)
car1 = Car('Audi Q5', 240, 18)

print(bus1.description())
print(car1.description())
# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
# Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18