""""
8. Napisati kod koji za dati pozitivni realni broj r računa i štampa obim i površinu kruga
poluprečnika r.

"""

import math

def obim_kruga(r):
    return 2*r*math.pi



def povrsina_kruga(r):
    return math.pow(r,2)*math.pi



r = float(input("Unesi poluprecnik: "))

print("Obim kruga:" , obim_kruga(r))
print("POvrsina kruga:" , povrsina_kruga(r))



