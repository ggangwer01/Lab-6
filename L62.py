#the authors names are Gwyn and Lily

def divisors(n):
    total = 0
    for x in range(1, n):
        if n % x == 0:
            total = total + x
    return total
def perfect():
    n=int(input("enter a number\n"))
    summ= divisors(n)
    if n == summ:
        return True
    else:
        return False
print(perfect())


