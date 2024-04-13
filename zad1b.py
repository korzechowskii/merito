liczby = list(range(1, 11))
print(liczby)

liczby.append(11)
print(liczby)

liczby.pop(2)
print(liczby)

indeksy_i_elementy = [(index, element) for index, element in enumerate(liczby)]
print(liczby)