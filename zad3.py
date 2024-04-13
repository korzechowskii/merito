# Inicjalizacja licznika
i = 1

# Lista przechowująca wyświetlane liczby
wyswietlone_liczby = []

# Pętla while wyświetlająca liczby od 1 do 10, ale przeskakuje 5 i kończy na 8
while i <= 10:
    if i == 5:
        i += 1
        continue
    if i > 8:
        break
    wyswietlone_liczby.append(i)
    i += 1

wyswietlone_liczby
print(wyswietlone_liczby)