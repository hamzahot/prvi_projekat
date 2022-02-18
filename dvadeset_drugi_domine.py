""""
22. (*) Domino se igra pločicama pravougaonog oblika, takvim da se na svakoj pločici nalaze
dvije oznake. Svaka oznaka sastoji se od određenog broja tačkica. Broj tačkica zavisi o
veličini skupa domina. U skupu domina veličine N broj tačkica na jednoj pločici može biti
bilo koji broj između 0 i N, uključivo. U jednom skupu ne postoje dvije pločice potpuno
jednakih oznaka, bez obzira na redosljed oznaka na pločici. U potpunom skupu veličine N
nalaze se sve moguće pločice sa oznakama 0 do N. Npr. potpuni skup domina veličine 2
sadrži šest pločica sa sljedećim oznakama:
Napišite program koji će odrediti ukupan broj tačkica na svim pločicama u potpunom
skupu domina veličine N. Vaš program treba da učita jedan prirodan broj N (1 ≤ N ≤ 1000)
– veličinu potpunog skupa domina. Program treba da štampa ukupan broj tačkica na svim
pločicama u potpunom skupu domina veličine N. 

"""



import math



def broj_domina(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    return int(n*(broj_domina(n-1)/(n-1)+n+1))
#rjesenje intuitivno , uocio sam semu...

n = int(input("Unesi N: "))
print(broj_domina(n))



