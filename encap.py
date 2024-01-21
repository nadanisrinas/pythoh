# Base class for cars
class Car:
   def __init__(self, make, model):
       self.make = make
       self.model = model


   def start_engine(self):
       print(f"The {self.make} {self.model}'s engine is now running.")


# Derived class ElectricCar, inheriting from Car
class ElectricCar(Car):
   def __init__(self, make, model, battery_capacity):
       # Call the base class constructor directly
       super().__init__(make, model)
       self.battery_capacity = battery_capacity


   def start_engine(self):
       # TODO tambahkan string "is now running with a battery capacity of ((variable battery capacity)) kWh."
       print(f"The {self.make} {self.model}'s electric motor is now running, is now running with a battery capacity of {self.battery_capacity} kWh.")


# Testing the classes
my_car = ElectricCar("Tesla", "Model S", 75)
my_car.start_engine()  # Output: The Tesla Model S's electric motor is now running.



