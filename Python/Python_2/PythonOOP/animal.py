class Animal(object):
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print self.name
        print self.health
        return self

class Dog(Animal):
    def __init__(self,name):
        super(Dog,self).__init__(name,150)

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self,name):
        super(Dragon,self).__init__(name,170)
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        print self.name
        print "Im a Dragon"
        return self

animal1 = Animal('Animal', 20)
animal1.walk().walk().walk().run().run().display_health()

dog = Dog('Fido')
dog.walk().walk().walk().run().run().pet().display_health()

dragon = Dragon("Smaug")
dragon.fly().display_health()


