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
car0 = Car("Merceds","c300",2020,80,5)
car1 = Car("BMW","e92",2025,150,5)
car2 = Car("Audi","A9",2023,80,4)
car3 = Car("kia","picanto",2020,20,4)
car4 = Car("Toyota","Corolla",2020,50,5)
bike=Bike("Yamaha","r1",2019,50,998)
bike0=Bike("Bmw","r9",2019,70,600)
bike1=Bike("v150","jaber",2019,10,150)
bike2=Bike("sweet","azzo",2019,10,125)
cars=[]
bikes=[]
cars.append(car)
cars.append(car0)
cars.append(car1)
cars.append(car2)
cars.append(car3)
cars.append(car4)
bikes.append(bike)
bikes.append(bike0)
bikes.append(bike1)
bikes.append(bike2)


bike.display_info()
print("________________________________________________________________________")
car.display_info()
print("________________________________________________________________________")
print(car.calculate_rental_cost(5))
print("________________________________________________________________________")
print(bike.calculate_rental_cost(15))
print("________________________________________________________________________")
car.setRental(55)
print("________________________________________________________________________")
print(car.calculate_rental_cost(5))
print("________________________________________________________________________")
def showVehicleInfo(Vehicle : Vehicles):
    Vehicle.display_info()
showVehicleInfo(car)
print("________________________________________________________________________")

stop = int(input("1 for cars 2 for bikes :"))
while stop !=0:
    count=0
    if stop ==1:
        for i in cars:
            print (f"{count}>>>>>>> ")
            i.display_info()
            print("**************************************************************************************************************************************")

            count+=1
    elif stop==2:
        for i in bikes:
            print (f"{count}>>>>>>> ")
            i.display_info()
            print("**************************************************************************************************************************************")
        
            count+=1
    else :
        print ("Choose a valid number")
    
    stop = int(input("1 for cars 2 for bikes 0 to quit:"))



