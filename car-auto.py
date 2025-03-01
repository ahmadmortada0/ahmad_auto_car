class Vehicals :
    def __init__ (self ,brand,model,year,rental):
        self.brand=brand 
        self.model=model
        self.year=int(year)
        self.__rental_price_per_day=int(rental)
    def display_info(self): 
        return f"the {self.brand} vehicals model is {self.model} and the module year is {self.year} and the rental price is {self.__rental_price_per_day}$"
    def calculate_rental_cost(self,days):
        return days*self.__rental_price_per_day
    def setRental(self,amount):
        self.__rental_price_per_day=amount
    def getRental(self):
        return self.__rental_price_per_day
    
class Car(Vehicals):
    def __init__(self, brand, model, year, rental,seating_capacity):
        super().__init__(brand, model, year, rental)
        self.seating_capacity=seating_capacity
    def display_info(self):
        print(super().display_info()+f" and seating capacity is {self.seating_capacity}")


car = Car("mer","C",2020,1500,4)
car.display_info()
# vehicals=[Vehicals]   
# v= Vehicals("Audi","r9",2026,150)
# print(v.calculate_rental_cost(20))
# v.display_info()

# stop=1
# stop = int(input("add a car/ if no press 0 : "))
# while stop !=0:
#      car_brand = input("Brand :")
#      car_model = input("model :")
#      car_year  = int(input("year :"))
#      car_rental_price = int(input("Price :"))
#      car= Vehicals(car_brand,car_model,car_year,car_rental_price)
#      vehicals.append(car)
#      stop = int(input("add another car/ if no press 0 : "))
# for vehical in vehicals:
#     vehical.display_info()
