class Vehicals :
    def __init__ (self ,brand,model,year,rental):
        self.brand=brand 
        self.model=model
        self.year=int(year)
        self.rental_price_per_day=int(rental)
    def display_info(self): 
        print(f"the {self.brand} vehicals model is {self.model} and the module year is {self.year} and the rental price is {self.rental_price_per_day}$")

vehicals=[Vehicals]   
v= Vehicals("Audi","r9",2026,150)
v.display_info()
stop=1
stop = int(input("add a car/ if no press 0 : "))
while stop !=0:
     car_brand = input("Brand :")
     car_model = input("model :")
     car_year  = int(input("year :"))
     car_rental_price = int(input("Price :"))
     car= Vehicals(car_brand,car_model,car_year,car_rental_price)
     vehicals.append(car)
     stop = int(input("add another car/ if no press 0 : "))
for vehical in vehicals:
    vehical.display_info()
    