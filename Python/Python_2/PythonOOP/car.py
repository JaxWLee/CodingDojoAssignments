class Car(object):
    def __init__(self,price,speed,fuel,milage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.milage = milage
        self.display_info()
    def display_info(self):
        print "Price:" + str(self.price)
        print "Speed:" + str(self.speed) +" MPH"
        print "Fuel:" + self.fuel
        print "Milage:" + str(self.milage)
        print "Tax:" + str(self.tax)
        print ""
        
car1 = Car(8000,55,"Full",18)
car2 = Car(12000,15,"Half",45)
