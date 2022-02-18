"""
7. Dato je rastojanje u centimetrima. Odrediti koliko cijelih metara ima u tom rastojanju. Npr.
324cm imaju 3 metra.

"""
import math

cm = int(input("Unesi duzinu u centimetrima: "))
print("Duzina u cijelim metrima je:" , cm//100)