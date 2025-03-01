class Vehicles :
    def __init__ (self ,brand,model,year,rental):
        self.brand=brand 
        self.model=model
        self.year=int(year)
        self.__rental_price_per_day=int(rental)
    def display_info(self): 
        return f"{self.brand}  {self.model}, Year  : {self.year}, Rental price : ${self.__rental_price_per_day}/day"
    def calculate_rental_cost(self,days):
        return f"Rental cost for {self.brand} {self.model} for {days} days is :${days*self.__rental_price_per_day}"
    def setRental(self,amount):
        if self.__rental_price_per_day!=amount:
          print(f"Updated rental price for {self.brand} {self.model} is : ${amount}/day")  
        self.__rental_price_per_day=amount
    def getRental(self):
        return self.__rental_price_per_day

        
    
class Car(Vehicles):
    def __init__(self, brand, model, year, rental,seating_capacity):
        super().__init__(brand, model, year, rental)
        self.seating_capacity=seating_capacity
       

    def display_info(self):
        print(f"Car :{super().display_info()} and seating capacity is {self.seating_capacity}")

class Bike(Vehicles):
    def __init__(self, brand, model, year, rental,engine_capacity):
        super().__init__(brand, model, year, rental)
        self.engine_capacity=str(engine_capacity)+"CC"

    def display_info(self):
        print(f"Bike :{super().display_info()} and the engine capacity is {self.engine_capacity}")


car = Car("Toyota","Corolla",2020,50,5)
bike=Bike("Yamaha","r1",2019,50,998)

bike.display_info()
car.display_info()
print(car.calculate_rental_cost(5))
print(bike.calculate_rental_cost(15))
car.setRental(55)
print(car.calculate_rental_cost(5))
def showVehicleInfo(Vehicle : Vehicles):
    Vehicle.display_info()
showVehicleInfo(car)
