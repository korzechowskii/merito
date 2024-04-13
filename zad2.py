# Tworzenie słownika angielsko-polskiego dla 5 słów
slownik = {
    "apple": "jabłko",
    "tree": "drzewo",
    "book": "książka",
    "car": "samochód",
    "sun": "słońce"
}

# Dodanie nowego tłumaczenia słowa
slownik["moon"] = "księżyc"

# Wyświetlenie tłumaczenia jednego z istniejących słów (np. "book")
tlumaczenie_book = slownik["book"]

# Używając pętli, wyświetlenie wszystkich angielskich słów wraz z ich polskimi tłumaczeniami
wszystkie_tlumaczenia = [(klucz, wartosc) for klucz, wartosc in slownik.items()]

tlumaczenie_book, wszystkie_tlumaczenia
print(tlumaczenie_book)
print(wszystkie_tlumaczenia)