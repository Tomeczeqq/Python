#Prosty przyklad uzycia programowania obiektowego w Pythonie

class osoba:
    pass                #nic

os1=osoba()             #automatycznie podczas wywolania powstal obiekt
os1.imie='Ala'
os1.nazwisko='Nowak'

class user:                                 #klasa
    def __init__(self,imie,nazwisko):       #metoda
        self.imie=imie
        self.nazwisko=nazwisko

u1=user("Ola","Kowalska")                  #nowy obiekt, ktory automatycznie wywoluje klase

''' Slowniczek pojec programowania obiektowego:
Obiekt - polaczenie danych i operacji na nich wykonywanych; unikatowy egzemplarz danych zdefiniowanych w jego klasie
Klasa - szablon, projekt, prototyp obiektu
Metoda - funkcja okreslona w definicji klasy
Dziedziczenie - przekazywanie charakterystyki klasy do innych klas
'''