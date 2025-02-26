class Vehicals :
    def __init__ (self ,brand,model,year,rental):
        self.brand=brand 
        self.model=model
        self.year=int(year)
        self.rental_price_per_day=int(rental)
    def display_info(self): 
        print(f"the {self.brand} vehicals model is {self.model} and the module year is {self.year} and the rental price is {self.rental_price_per_day}$")


v= Vehicals("Audi","r9",2026,150)
v.display_info()