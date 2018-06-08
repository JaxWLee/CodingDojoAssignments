class Products(object):
    def __init__(self,price,name,weight,brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"

    def sell(self):
        self.status = "Sold"
        return self
    
    def addtax(self,tax_amount):
        self.tax = tax_amount
        print self.price + (self.price * self.tax)
        return self

    def returning(self,reason,condition):
        self.reason = reason
        self.condition = condition
        if self.condition == "In Box":
            self.status = "For Sale"
        elif self.condition == "Opened":
            self.status = "Used"
            self.price = self.price - (self.price * 0.2)
        elif self.condition == "Defective":
            self.status = self.condition
        return self
    
    def display_info(self):
        print self.name
        print "Price: $" + str(self.price)
        print "Brand: " + self.brand 
        print "Wieght: " +str(self.weight) +"lbs"
        print self.status
        print
        return self

product1= Products(10,"Paper",1.5,"Dunder Miflen")
product2 = Products(25,"Space Pen",3,"NASA")
product2a = Products(25,"Space Pen",3,"NASA")
product2b = Products(25,"Space Pen",3,"NASA")
product3 = Products(1000,"Iapple",.7,"Apple")

product1.addtax(0.05).sell().display_info()

product2.addtax(0.05).sell().returning("Broken","Defective").display_info()
product2a.sell().returning("Unwanted","In Box").addtax(0.05).display_info()
product2b.sell().returning("Wrong Product","Opened").addtax(0.05).display_info()

product3.addtax(0.1).sell().display_info().returning("Unwanted","Opened").display_info()

