class bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayinfo(self):
        print("Price is $", self.price)
        print("Maxium speed is", self.max_speed,"MPH")
        print("Total Miles" , self.miles ,"miles")
        return self
    
    def ride(self):
        print('Riding')
        self.miles += 10

    def reverse(self):
        print('Reversing')
        self.miles -= 5


new_bike = bike(13000,300)
new_bike.ride()
new_bike.ride()
new_bike.ride()
new_bike.reverse()
new_bike.displayinfo()


new_bike1 = bike(10000,200)
new_bike1.ride()
new_bike1.ride()
new_bike1.reverse()
new_bike1.reverse()
new_bike1.displayinfo()


new_bike2 = bike(500,10)
new_bike2.reverse()
new_bike2.reverse()
new_bike2.reverse()
new_bike2.displayinfo()