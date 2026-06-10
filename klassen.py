
class Gebaeude:

    def __init__(self, anzahl_etagen):
        self.attribut_anzahl_etagen = anzahl_etagen

    def sag_hallo(self):
        print("Hallo, ich habe", self.attribut_anzahl_etagen, "Etagen")

industriehalle = Gebaeude(anzahl_etagen=3)
industriehalle.sag_hallo()

import random

class Wuerfel:

    def __init__(self, farbe, groesse):
        self.farbe = farbe
        self.groesse = groesse

    def drehen(self):
        return random.randint(1,6)
    
kleiner_roter_wuerfel = Wuerfel("rot", 6)
zahl = kleiner_roter_wuerfel.drehen()
print(zahl)

grosser_schwarzer_wuerfel = Wuerfel("schwarz", 100)
zahl = grosser_schwarzer_wuerfel.drehen()
print(zahl)

class Student:

    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def geburtstag(self):
        self.alter = self.alter + 1

    def infos(self):
        print("Ich heiße", self.name, "und bin ", self.alter, "jahre alt")

peter = Student("Peter", 20)
peter.infos()
peter.geburtstag()
peter.infos()
print(peter.name)
print(peter.alter)


# Aufgabe 1
class Konto:

    def __init__(self, kontoinhaber, kontostand=0):
        self.kontoinhaber = kontoinhaber
        self.kontostand = kontostand

    def einzahlen(self, betrag):
        self.kontostand = self.kontostand + betrag

    def abheben(self, betrag):
        if self.kontostand >= betrag:
            self.kontostand = self.kontostand - betrag
        else:
            print("Nicht genug Guthaben vorhanden.")

    def kontostand_anzeigen(self):
        print(f"Der Kontostand beträgt: {self.kontostand}")

mein_konto = Konto(kontoinhaber="Peter", kontostand=0)

# betrag = float(input("Wieviel willst du einzahlen?"))
mein_konto.einzahlen(100)
mein_konto.kontostand_anzeigen()

# betrag = float(input("Wieviel willst du abheben?"))
mein_konto.abheben(10)

# Aufgabe Gabaeude

class Gebaeude:

    def __init__(self, anzahl_etagen, strasse, anzahl_raeume):
        self.anzahl_etagen = anzahl_etagen
        self.strasse = strasse
        self.anzahl_raeume = anzahl_raeume

    def renovieren(self):
        self.anzahl_raeume = self.anzahl_raeume + 1 

    # def __repr__(self):
    #     return f"Ich habe {self.anzahl_etagen} Etagen"

    def __str__(self):
        return f"Ich habe {self.anzahl_etagen} Etagen"
    
    def __len__(self):
        return self.anzahl_raeume
    
    def __eq__(self, other):
        return self.anzahl_raeume == other.anzahl_raeume
    
wohnhaus = Gebaeude(2, "Musterstrasse", 6)
lagerhalle = Gebaeude(1, "Musterstrasse", 1)

print(wohnhaus.anzahl_raeume)
wohnhaus.renovieren()
print(wohnhaus.anzahl_raeume)

print(wohnhaus)
print(len(wohnhaus))

if wohnhaus == lagerhalle:
    print("Sind gleich!")
else:
    print("nicht gleich!")
