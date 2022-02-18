""""
17. Napisati kod koji za date realne brojeve x i y provjerava da li tačka sa koordinatama (x,y)
pripada osjenčenom dijelu ravni. Centar oba kruga je u tački (0,0), poluprečnici su im
redom 4 i 6, dok je prava data jednačinom x-y-4=0. Podsjetite se da je krug skup tačaka u
ravni koje su na rastojanju r od date tačke tj. centra kruga. Štampati poruku „Pripada“ ili
„Ne pripada“. 
"""
import math

def osjenceni_dio(x,y):
    print(math.pow(x,2)+math.pow(y,2))
    if (math.pow(x,2) + math.pow(y,2))<=36 and (math.pow(x,2)+math.pow(y,2))>=16 and x<=0 and y>=0:
        return True
    elif (math.pow(x,2)+math.pow(y,2))<=16 and x>=0 and y>=0:
        return True
    elif (math.pow(x,2)+math.pow(y,2))<=16 and y < x-4:
        return True
    elif (math.pow(x,2)+math.pow(y,2))<=36 and (math.pow(x,2)+math.pow(y,2))>=16 and x>=0 and y>=0 and y<x-4:
        return True
    else:
        return False

x = float(input("Unesi x: "))
y = float(input("Unesi y: "))


if osjenceni_dio(x,y):
    print("Pripada")
else:
    print("Ne pripada")