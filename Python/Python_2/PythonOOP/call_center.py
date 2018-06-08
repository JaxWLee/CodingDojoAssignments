import datetime
class Call(object):
    number = 0
    def __init__(self,name,number,reason):
        self.id = Call.number
        self.name = name
        self.number = number
        self.reason = reason
        self.time = datetime.datetime.now()
        Call.number += 1
    def display(self):
        print "\n" + ("#" * 20)
        for attr, val in self.__dict__.iteritems():
            if attr == "time":
               print "{}: {}".format(attr,val.strftime("%I:%M:%S"))
            else:
                 print "{}: {}".format(attr,val)
        print "#" * 20
md1 = Call('Jame',914,"you know")
md2 = Call('James',212,"youknow")
md1.display()
md2.display()

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.qsize = self.getqsize()
    def getqsize(self):
        return len(self.calls)
    def add(self,name,number):
        self.new_caller = name 
        self.new_number = number
        self.new_time = datetime.datetime.now()
        

        