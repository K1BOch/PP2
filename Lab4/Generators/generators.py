def squares():
    n = int(input())
    sq = (int(i)**2 for i in range(0, n))
    for i in range(n):
        print(next(sq))

def evens():
    n = int(input())
    ev = (int(i) for i in range(0, n, 2))
    for i in range(int(n/2)):
        print(next(ev), end = ", ")
    print(next(ev))
    
def divisibility():
    n = int(input())
    x = lambda x : x if(x % 3 == 0 and x % 4 == 0 and x != 0) else "o"
    a = (x(i) for i in range(0, n))
    for i in range(n):
        y = next(a)
        if(y != "o"):
            print(y)

def squareatob():
    a = int(input())
    b = int(input())
    sq = (int(i)**2 for i in range(a, b+1))
    for i in range (b - a + 1):
        print(next(sq))

def fromnto0():
    n = int(input())
    decr = (int(i) for i in range (n, 0, -1))
    for i in range(n):
        print(next(decr))

squares()
evens()
divisibility()
squareatob()
fromnto0()