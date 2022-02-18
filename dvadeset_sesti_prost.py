""""
26. Napisati metod boolean jeProst(int n) koji za dati broj n provjerava da li je prost, i
ako jeste, vraća true, a ako nije, vraća false. 


28. Napisati metod void prostiDjelioci(int n) koji za dati broj n štampa sve proste
djelioce broja n.

"""

#Znam da ste ovaj vec radili ali eto optimalnija verzija...

import math

def prost(n):
    i=2
    if n==1:
        return False
    if n==2:
        return True
    while i<=math.ceil(math.sqrt(n)):
        if n%i == 0:
            return False
        i+=1
    return True


n = int(input("Unesi broj: "))

if prost(n):
    print("Broj je prost")
else:
    print("Nije prost")




""""
28. Napisati metod void prostiDjelioci(int n) koji za dati broj n štampa sve proste
djelioce broja n.

"""


def prosti_djelioci(n):
    for i in range (1,n+1):
        if n%i==0 and prost(i):
            print(i)


s = int(input("Unesi broj: "))
print("Njegovi prosti djelioci: ")
prosti_djelioci(s)