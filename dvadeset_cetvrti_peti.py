""""
24. Napisati kod koji za datu godinu odreñuje da li je prestupna i štampa odgovarajuću
poruku.

25. Napisati kod koji za dati redni broj mjeseca (od 1 do 12) i datu godinu štampa broja dana u
datom mjesecu.

"""



def prestupna(god):
    if god%100 == 0:
        if god%400 == 0:
            return True
        else:
            return False
    elif god%4 == 0:
        return True
    else:
        return False


def broj_dana(mjesec , godina , broj_dana_po_mjesecu):
    if prestupna(godina) and mjesec == 2:
        return 29
    else:
        return broj_dana_po_mjesecu[mjesec-1]


broj_dana_po_mjesecu = [31,28,31,30,31,30,31,31,30,31,30,31]

mjesec = int(input("Unesite redni broj mjeseca(1-12): "))
godina = int(input("Unesite godinu: "))


if prestupna(godina):
    print("Prestupna")
else:
    print("Nije prestupna")



print("Unijeti mjesec ima:" , broj_dana(mjesec , godina , broj_dana_po_mjesecu) , "dana")
