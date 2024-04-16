from datetime import datetime

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar
        self.foglalt_datumok = []

    def foglalas(self, datum):
        if datum in self.foglalt_datumok:
            print(f"A szoba {self.szobaszam} már foglalt {datum}-ra.")
            return False
        else:
            self.foglalt_datumok.append(datum)
            print(f"Szoba {self.szobaszam} foglalva {datum}-ra. Ár: {self.ar} Ft")
            return self.ar

    def lemondas(self, datum):
        if datum in self.foglalt_datumok:
            self.foglalt_datumok.remove(datum)
            print(f"Foglalás lemondva a szobában {self.szobaszam} ezen a napon: {datum}")
            return True
        else:
            print(f"Nincs foglalás ezen a napon a szobában {self.szobaszam}.")
            return False

    def foglalas_ara(self, datum):
        if datum in self.foglalt_datumok:
            return self.ar
        else:
            return 0

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def szoba_hozzaadasa(self, szobaszam, ar):
        self.szobak.append(Szoba(szobaszam, ar))

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                if datetime.now().date() < datum:
                    return szoba.foglalas(datum)
                else:
                    print("Hibás dátum. Csak jövőbeli foglalás lehetséges.")
                    return None
        print("Nincs ilyen szoba a szállodában.")
        return None

    def lemondas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                return szoba.lemondas(datum)
        print("Nincs ilyen szoba a szállodában.")
        return False

    def osszes_foglalas_listazasa(self):
        for szoba in self.szobak:
            for datum in szoba.foglalt_datumok:
                print(f"Szoba: {szoba.szobaszam}, Dátum: {datum}")

    def foglalas_ara(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                return szoba.foglalas_ara(datum)
        print("Nincs ilyen szoba a szállodában.")
        return 0

def felhasznaloi_interfesz(szalloda):
    print("Üdvözöljük a Szállodai Szobafoglaló Rendszerben!")
    while True:
        print("\nVálasszon a következő lehetőségek közül:")
        print("1. Szobák listázása")
        print("2. Szoba hozzáadása")
        print("3. Szoba törlése")
        print("4. Foglalás")
        print("5. Lemondás")
        print("6. Foglalások listázása")
        print("7. Kilépés")

        valasztas = input("Kérem, válasszon egy lehetőséget (1/2/3/4/5/6/7): ")

        if valasztas == "1":
            print("Rendelkezésre álló szobák:")
            for szoba in szalloda.szobak:
                print(f"Szobaszám: {szoba.szobaszam}, Ár: {szoba.ar} Ft")
        elif valasztas == "2":
            szobaszam = input("Kérem, adja meg az új szoba sorszámát: ")
            ar = int(input("Kérem, adja meg az új szoba árát (Ft-ban): "))
            szalloda.szoba_hozzaadasa(szobaszam, ar)
            print("Az új szoba hozzáadva.")
        elif valasztas == "3":
            szobaszam = input("Kérem, adja meg a törölni kívánt szoba sorszámát: ")
            for szoba in szalloda.szobak:
                if szoba.szobaszam == szobaszam:
                    szalloda.szobak.remove(szoba)
                    print(f"A(z) {szobaszam} sorszámú szoba törölve.")
                    break
            else:
                print("Nincs ilyen szoba a szállodában.")
        elif valasztas == "4":
            szobaszam = input("Kérem, adja meg a foglalni kívánt szoba sorszámát: ")
            datum_str = input("Kérem, adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            datum = datetime.strptime(datum_str, "%Y-%m-%d").date()
            szalloda.foglalas(szobaszam, datum)
        elif valasztas == "5":
            szobaszam = input("Kérem, adja meg a lemondani kívánt foglalás szoba sorszámát: ")
            datum_str = input("Kérem, adja meg a lemondani kívánt foglalás dátumát (YYYY-MM-DD formátumban): ")
            datum = datetime.strptime(datum_str, "%Y-%m-%d").date()
            szalloda.lemondas(szobaszam, datum)
        elif valasztas == "6":
            szalloda.osszes_foglalas_listazasa()
        elif valasztas == "7":
            print("Kilépés...")
            break
        else:
            print("Hibás választás!")

def main():
    # Teszt adatok létrehozása
    szalloda = Szalloda("Teszt Szalloda")
    szalloda.szoba_hozzaadasa("101", 5000)
    szalloda.szoba_hozzaadasa("102", 6000)
    szalloda.szoba_hozzaadasa("103", 7000)

    # Teszt adatokkal való futtatás
    felhasznaloi_interfesz(szalloda)

if __name__ == "__main__":
    main()
