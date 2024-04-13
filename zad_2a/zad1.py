# Tworzenie listy liczb od 1 do 10
liczby = list(range(1, 11))

# Dodanie liczby 11 na koniec listy
liczby.append(11)

# Usunięcie trzeciego elementu listy (indeks 2)
liczby.pop(2)

# Wypisanie każdego elementu listy wraz z jego indeksem
indeksy_i_elementy = [(index, element) for index, element in enumerate(liczby)]

liczby, indeksy_i_elementy
