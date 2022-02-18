""""
18. Dato je 6 realnih promjenljivih a1, a2, b1, b2, c1, c2. Odrediti da li postoji trougao čija su
tjemena A(a1,a2), B(b1,b2) i C(c1,c2) i štampati odgovarajuću poruku (npr. „Postoji“).

"""

import math

def duzina_stranice(x1,y1,x2,y2):
    return math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))


def trougao(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False


a1 = float(input("Unesi a1: "))
a2 = float(input("Unesi a2: "))
b1 = float(input("Unesi b1: "))
b2 = float(input("Unesi b2: "))
c1 = float(input("Unesi c1: "))
c2 = float(input("Unesi c2: "))


a = duzina_stranice(b1,b2,c1,c2)
b = duzina_stranice(a1,a2,c1,c2)
c = duzina_stranice(a1,a2,b1,b2)

if trougao(a,b,c):
    print("Postoji")
else:
    print("Ne postoji")