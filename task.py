class CarsDetails:
    carName: str
    carModel: str
    carColor: str

    def printCarDetails(self):
        print(f"Name: {self.carName}, Model: {self.carModel}, Color: {self.carColor}")

print("Enter the car details")
car1 = CarsDetails()
car1.carName = input("Enter the car name: ")
car1.carModel = input("Enter the car model: ")
car1.carColor = input("Enter the car color: ")
car1.printCarDetails()