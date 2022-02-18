"""
8. Napisati metod int zbirCifara(int n) koji vraća zbir cifara broja n. 
"""


import math

def zbir_cifara(n):
    suma=0

    while n>0:
        cifra = int(n%10)
        suma+=cifra
        n/=10

    return suma




n = int(input("Unesi broj n: "))
print("Zbir cifara broja n:" , zbir_cifara(n))