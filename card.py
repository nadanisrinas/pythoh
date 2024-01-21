class Car:
  def __init__(self, make, model, year, color):
      # Initialize the attributes
      self.make = make
      self.model = model
      self.year = year
      self.color = color
      self.speed = 0


  def accelerate(self, speed_increase):
      # Increase the speed of the car by the given amount
      self.speed += speed_increase


  def brake(self, speed_decrease):
        # if speed_decrease >  self.speed:
        #     self.speed = 0
        # else:
        #     self.speed -= speed_decrease
      self.speed -= speed_decrease
      self.speed = max(0, speed_decrease)
        

  def honk(self):
      # Print a honking message
      print("Honk! Honk!")


  def display_info(self):
      # Print the information about the car (make, model, year, color, speed)
      print(f"{self.year} {self.make} {self.model}, {self.color}")
      print(f"Current Speed: {self.speed} mph")


def main():
   # Call class:
   my_car = Car(make="Toyota", model="Camry", year=2022, color="Blue")

   # Accelerate the car
   my_car.accelerate(100)


   # Display car information
   my_car.display_info()


   # Brake the car
   my_car.brake(120)


   # Display updated information
   my_car.display_info()


   # Honk the horn
   my_car.honk()

if __name__ == "__main__":
    main()
 
