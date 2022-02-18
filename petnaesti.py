import math

def funkcija(x):
    if x>0:
        return math.sin(2*x+5)
    else:
        c = -2*math.pow(2,x)+7/2
        return c


x = int(input("Unesi broj x: "))
print(funkcija(x))