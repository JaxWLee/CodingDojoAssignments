class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self,*args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for k in i:
                    self.result += k
            else:
                self.result += i
        return self
    def subtract(self,*args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                self.sum = 0
                for k in i:
                    self.sum += k
                    self.result -= self.sum
            else:
                self.result -= i
        return self
md = MathDojo()
md = md.add(2).add(2,5).subtract(3,2)
print md.result
md = md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3])
print md.result
        