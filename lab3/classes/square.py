
class Shape():
    area = 0

class Square(Shape):
    def __init__(self, length = 0):
        self.length = length
    
    def area(self):
        return (self.length ** 2)


x = int(input())
s = Square(x)
print(s.area())

print(Square(2).area())