class Shape():
    area = 0
    

class Rectangle(Shape):
    def __init__(self, length = 0, width = 0):
        self.length = length
        self.width = width
    
    def display(self):
        self.area = self.length * self.width
        return self.area

l = int(input())
w = int(input())
r = Rectangle(l,w)
print(r.display())


print(Rectangle(4,4).display())