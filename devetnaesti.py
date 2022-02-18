"""
19. (*) Dat je cio broj k (1<=k<=180) i niz cifara 10111213...9899 koji se dobija kada se svei
dvocifreni brojevi redom zapišu jedna iza drugog. Za dato k, odrediti dvocifreni broj koji sadrži
k-tu cifru u datom nizu. Npr., za k=7, traženi broj je 13. 

"""
def broj(k , niz):
    if k%2==0:
        return niz[k] + 10*niz[k-1]
    else:
        return 10*niz[k] + niz[k+1]

niz = [1,0,1,1,1,2,1,3,1,4,1,5,1,6,1,7,1,8]
k = int(input("Unesi broj k: "))


