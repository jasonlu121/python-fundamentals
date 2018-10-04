class product:
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    
    def sell(self):
            self.sell = "sold"


    def add_tax(self):
        self.price = self.price *1.09


    def return_item(self, reason_for_return):
        if(reason_for_return == 'defective'):
            self.status = 'defective'
            self.price = 0
        if(reason_for_return == 'like_new'):
            self.status = 'for sale'
        if(reason_for_return == 'opened'):
            self.status = 'used'
            self.price = self.price * 0.8

    def display_info(self):
        print ('Price: $', self.price)
        print ('item_name: ', self.item_name)
        print ('weight: ', self.weight,'lbs')
        print ('brand: ', self.brand)
        print ('status', self. status)
     
    

product1 = product(200, 'all-saints chelsea boots', 15, 'all-saints')
product1.return_item('opened')
product1.add_tax()
product1.sell()
product1.display_info()