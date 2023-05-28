
class IMath:
    def add(self, x, y):
        raise NotImplementedError()

    def sub(self, x, y):
        raise NotImplementedError()

    def mul(self, x, y):
        raise NotImplementedError()

    def div(self, x, y):
        raise NotImplementedError()

class Math(IMath):
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y

class Proxy(IMath):

    def __init__(self):
        self.math = Math()

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return self.math.mul(x, y)

    def div(self, x, y):
        return float('inf') if y == 0 else self.math.div(x, y) 

p = Proxy()
x, y = 4, 2
print ('4 + 2 = ' + str(p.add(x, y)))
print ('4 - 2 = ' + str(p.sub(x, y)))
print ('4 * 2 = ' + str(p.mul(x, y)))
print ('4 / 2 = ' + str(p.div(x, y)))