import math
def degtorad():
    deg = int(input("Input degree: "))
    return f"Output radian: {math.radians(deg)}"

def trapezoidarea():
    h = int(input("Height: "))
    f = int(input("Base, first value: "))
    s = int(input("Base, second value: "))
    area = ((f+s) / 2) * h
    return area

def polygonarea():
    s = int(input("Input number of sides: "))
    l = int(input("Input the length of a side: "))
    area = (s * l**2) / (4 * math.tan(math.pi/s))
    return f"The area of the polygon is: {round(area)}"

def parallelogramarea():
    l = int(input("Length of base: "))
    h = int(input("Height of parallelogram: "))
    area = float(l * h)
    return f"Expected output: {area}"


print(degtorad())
print(trapezoidarea())
print(polygonarea())
print(parallelogramarea())