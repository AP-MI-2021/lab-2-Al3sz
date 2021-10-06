def get_base_16_from_2(n: str) -> str:
    '''
    Convertirea numărului din baza 2 în baza 16.
    :param n:
    :return:
    '''
    n1=n
    nr = 2
    deci = int(n,2)
    hexi = hex(deci)
    # Aici am convertit string-ul de intrare cu funcția int() în baza 10, iar apoi in baza hexazecimală cu funcția hex().
    print(f'Numărul {n} din baza 2 convertit în baza 16 este: {hexi[2:]}')

def test_get_base_16_from_2():
    '''
    Teste pentru funcția get_base_16_from_2().
    :return:
    '''
    assert get_base_16_from_2(100)
    assert get_base_16_from_2(1001)
    assert get_base_16_from_2(1101)
    assert get_base_16_from_2(10011)

def get_n_choose_k(n: int, k: int) -> int:
    '''
    Calcularea combinărilor de n luate câte k.
    :param n:
    :param k:
    :return:
    '''
    n1=n
    k1=k
    p = n - k
    nfac=1
    kfac=1
    pfac=1
    # Aici am creat variabilele nfac, kfac și pfac pentru a reprezenta n!, k!, si p! = (n-k)!. În final am folosit formula Cn luate cate k= n!/k!(n-k)!.
    while n > 1:
        nfac = nfac * n
        n-=1
    while k > 1:
        kfac = kfac * k
        k-=1
    while p > 1:
        pfac = pfac * p
        p-=1
    comb = nfac // (pfac * kfac)
    print(f'Rezultatul combinărilor de {n1} luate câte {k1} este: {comb}.')

def test_get_n_choose_k():
    '''
    Teste pentru funcția get_n_choose_k().
    :return:
    '''
    assert get_n_choose_k(5,2)
    assert get_n_choose_k(6,3)
    assert get_n_choose_k(10,8)
    assert get_n_choose_k(21,16)

def get_leap_years(start: int, end: int) -> list[int]:
    '''
    Afișarea sub formă de lista a anilor bisecți între doi ani dați.
    :param start:
    :param end:
    :return:
    '''
    start1=start
    end1=end
    a = []
    # Aici am creat o lista în care să rețin anii bisecți cuprinși în intervalul anilor dați. Am verificat mai apoi proprietățile anilor bisecți.
    while start <= end :
        if start % 4 == 0 and start % 100 != 0:
            a.append(start)
        elif start % 400 == 0 and start % 100 ==0 :
            a.append(start)
        start += 1
    print(f'Lista anilor bisecti cuprinși între anii {start1} și {end1} este: {a}')
def test_get_leap_years():
    '''
    Teste pentru funcția get_leap_years().
    :return:
    '''
    assert get_leap_years(1920, 2300)
    assert get_leap_years(2002, 2004)
    assert get_leap_years(2000, 2000)
    assert get_leap_years(62, 6500)

def main():
    '''
    Funcția main pentru rulare de
    :return:
    '''
    print('1. Convertește un număr din baza 2 în baza 16.')
    print('2. Calculează combinări de n luate câte k.')
    print('3. Afișează toți anii bisecți între doi ani dați.')
    print('x. Închide.')
    opt = input('Alege una dintre variantele menționate mai sus: ')
    if opt == '1':
        n = input('Atribuiți un număr în baza 2: ')
        get_base_16_from_2(n)
    elif opt == '2':
        n = int(input('Alegeți termenul n: '))
        k = int(input('Alegeți termenul k: '))
        get_n_choose_k(n, k)
    elif opt == '3':
        an1 = int(input('Tastați primul an: '))
        an2 = int(input('Tastați al doilea an: '))
        get_leap_years(an1, an2)
    elif opt == 'x':
        print('')

if __name__ == '__main__':
    main()
