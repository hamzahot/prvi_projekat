"""
29. Napisati metod int gcd(int n, int m) koji vraća najveći zajednički djelilac brojeva m
i n. (Pogledati na internetu Euklidov algoritam).

"""

def nzd(m,n):
    if n==0:
        return m
    return nzd(n , m%n)


m = int(input("Unesi broj m: "))
n = int(input("Unesi broj n: "))

print("NZD brojeva m i n je:" , nzd(m,n))