"""
15. Dat je četvorocifren broj. Odrediti broj koji se dobija zamjenom treće i druge cifre. Npr. od
5804 dobija se 5084.

"""

    

import math

def zamjena(n):
    cetvrta=n%10
    treca=(n//10)%10
    druga=(n/100)%10
    prva=n//1000
    return int(prva*1000+treca*100+druga*10+cetvrta)


n = int(input("Unesi cetvorocifreni broj: "))
print(zamjena(n))
print(5804%10)

