class Bike(object):
    def __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def display_info(self):
        print "Price: "+ str(self.price) + ", Max Speed: " + str(self.max_speed) +" MPH" + ", Miles Ridden: " + str(self.miles)
        return self

    def ride(self):
        print "Riding.."
        self.miles += 10
        return self

    def reverse(self):
        if self.miles == 0:
            print "Cannot have negative miles ridden"
            self.miles += 0
            return self
        else:
            print "Reversing..."
            self.miles -= 5
            return self

bike1 = Bike(300,30)
bike1.ride().ride().ride().reverse().display_info()
bike2 = Bike(300,30)
bike2.ride().ride().reverse().reverse().display_info()
bike3 = Bike(250,25)
bike3.ride().reverse().display_info().reverse().reverse().reverse().display_info()
bike3 = Bike(200,15).ride().display_info()

# All methods are chainable. The only thing you could not do is use __init__ twice whithin a single statement as you would need to difine another varialbe for the second instantiation # 