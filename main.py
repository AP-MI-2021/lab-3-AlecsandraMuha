def isPrime(x):
    '''
    determina daca un nr. este prim
    :param x: un numar intreg
    :return: True, daca x este prim sau False in caz contrar
    '''
    if x < 2:
        return False
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    return True
def nr_divizori(n):
    '''
    se calculeaza numarul de divizori ai lui n
    :param n: nr intreg
    :return: nr de divizori ai lui n
    '''
    if n==0:
        return 0
    if n==1:
        return 1
    nr=2
    for i in range(2,n//2+1):
        if n % i == 0:
            nr+=1
    return nr
def toateelemprime(l):
    '''
    determina daca toate nr. dintr-o lista sunt prime
    :param l: lista de nr. intregi
    :return: True, daca toate nr. din l sunt prime sau False, in caz contrar
    '''
    for x in l:
        if isPrime(x) == False:
             return False
    return True
def get_longest_all_primes(l):
    '''
    determina cea mai lunga subsecventa de nr. prime
    :param l: lista de nr. intregi
    :return: cea mai lunga subsecventa de nr. prime din l
    '''
    subsecventaMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if toateelemprime(l[i:j+1]) and len(l[i:j+1]) > len(subsecventaMax):
                subsecventaMax = l[i:j+1]
    return subsecventaMax
def test_get_longest_all_primes():
    assert get_longest_all_primes([]) == []
    assert get_longest_all_primes([5,6,6]) == [5]
    assert get_longest_all_primes([11,11,11]) == [11,11,11]
    assert get_longest_all_primes([11,23,3,10]) == [11,23,3]
def toateelemacnrdiv(l):
    '''
    se verifica daca toate elementele din lista au acelasi nr de divizori
    :return: False daca nr de divizori difera, iar True in caz contrar
    '''
    nr_div1=nr_divizori(l[0])
    for i in l:
        if nr_divizori(i)!=nr_div1:
            return False
    return True
def get_longest_same_div_count(l):
    '''
    - determina cea mai lunga subsecventa de numere ce au acelasi numar de divizori
   '''
    secv_max=[]
    for i in range(len(l)):
        for j in range(i,len(l)):
            if toateelemacnrdiv(l[i:j+1]) and len(l[i:j+1])>=len(secv_max):
                secv_max=l[i:j+1]
    return secv_max
def test_get_longest_same_div_count():
    assert get_longest_same_div_count([7, 2,3,8]) == [7,2,3]
    assert get_longest_same_div_count([12,23,5,9,11]) == [23,5]
    assert get_longest_same_div_count([2,2,2,2]) == [2,2,2,2]
    assert get_longest_same_div_count([]) == []

def printMenu():
    print("1. Citire lista")
    print("2. Afisare cea mai lunga subsecventa de nr. prime")
    print("3. Afisare cea mai lunga subsecventa de nr. cu acelasi nr de divizori.")
    print("4. Iesire")

def citireLista():
    l = []
    n = int(input("Dati nr. de elemente: "))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]=")))
    return l
def main():
    test_get_longest_all_primes()
    test_get_longest_same_div_count()
    l = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print(get_longest_all_primes(l))
        elif optiune == "3":
            print(get_longest_same_div_count(l))
        elif optiune == "4":
            break
        else:
            print("Optiune gresita! Alege alta optiune!")

if __name__ == '__main__':
    test_get_longest_all_primes()
    test_get_longest_same_div_count()
main()