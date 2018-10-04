class car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if (self.price>10000):
            self.tax = 0.15
        else:
            self.tax = 0.12


    def display_all(self):
        print ('Price: $', self.price)
        print ('Speed: ', self.speed,'MPH')
        print ('Fuel: ', self.fuel)
        print ('Mileage:', self.mileage, 'mpg')
        print ('Tax:', self.tax)
    

car1 = car(2000, 35, 'Full', 15)
car2 = car(2000, 5, 'Not Full', 105)
car3 = car(2000, 15, 'Kind of Full', 95)
car4 = car(2000, 25, 'Full', 25)
car5 = car(2000, 45, 'Empty', 25)
car6 = car(20000000, 35, 'Empty', 15)


car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()