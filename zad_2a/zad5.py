class ZarzadcaZasobow:
    def __init__(self):
        self.zasoby = {}

    def dodaj_zasob(self, nazwa, zasob):
        self.zasoby[nazwa] = zasob

    def usun_zasob(self, nazwa):
        if nazwa in self.zasoby:
            del self.zasoby[nazwa]

    def pokaz_zasoby(self):
        for nazwa, zasob in self.zasoby.items():
            print(f"{nazwa}: {zasob}")

# Użycie klasy
zarzadca = ZarzadcaZasobow()
zarzadca.dodaj_zasob("Drukarka", {"model": "HP LaserJet", "status": "dostępna"})
zarzadca.dodaj_zasob("Projektor", {"model": "Epson EB-U05", "status": "w użyciu"})
zarzadca.pokaz_zasoby()
