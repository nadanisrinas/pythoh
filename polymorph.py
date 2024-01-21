class Car:
    def __init__(self, make, model, year):
        self.make =  make
        self.model =  model
        self.year = year

    def start(self):
        print(f"{self.make} {self.model} started.")
    def stop(self):
        print(f"{self.make} {self.model} stopped.")
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make,model,year)
        self.battery_capacity = battery_capacity
    def start(self):
        print(f" {self.make} {self.model} started silently.")
# Create a list of Car objects
Car_obj = [Car("Toyota", "Corolla", 2822), ElectricCar("Tesla", "Model S", 2015, "98.0 kWh")]
# Call the start method on each object
for i in Car_obj:
    print(i.start())

print(len(Car_obj))
