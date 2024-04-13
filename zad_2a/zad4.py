# Definicja funkcji sumującej liczby w liście
def sumuj_liczby(lista_liczb):
    if not lista_liczb:  # Sprawdzenie, czy lista jest pusta
        return 0
    else:
        return sum(lista_liczb)

# Testowanie funkcji z kilkoma różnymi listami
test1 = sumuj_liczby([1, 2, 3, 4, 5])  # Lista z wartościami
test2 = sumuj_liczby([])              # Pusta lista

test1, test2
print(test1)
print(test2)