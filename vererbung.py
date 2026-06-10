class Person:

    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def geburtstag(self):
        self.alter = self.alter + 1

class Student(Person):

    def __init__(self, name, alter, note):
        super().__init__(name, alter)
        self.note = note

class Dozent(Person):

    def __init__(self, name, alter, gehalt):
        super().__init__(name, alter)
        self.gehalt = gehalt

peter = Person("Peter", 21)
maria = Student("Maria", 19, 1)
print(maria.alter)
maria.geburtstag()
print(maria.alter)

alfred = Dozent("Alfred", 30, 1000)
print(alfred.alter)
alfred.geburtstag()
print(alfred.alter)


class Bank:

    def __init__(self, name, tagesgeldzinsen):
        self.name = name
        self.tagesgeldzinsen = tagesgeldzinsen

    def berechne_rendite(self, betrag):
        return betrag * (1+self.tagesgeldzinsen)


class Sparkkasse(Bank):

    def __init__(self, name, tagesgeldzinsen):
        super().__init__(name, tagesgeldzinsen)

    def berechne_rendite(self, betrag):
        return betrag * (1+self.tagesgeldzinsen) - 5
    
class Raiffeisen(Bank):

    def __init__(self, name, tagesgeldzinsen):
        super().__init__(name, tagesgeldzinsen)

    def monatsgebühren(self):
        print("keine Monatsgebühren")

sparkasse = Sparkkasse("Sparkasse Detmold", 0.04)
print(sparkasse.berechne_rendite(1000))

raiffeisen = Raiffeisen("Raiffeisenbank Berlin", 0.03)
raiffeisen.monatsgebühren()
print(raiffeisen.berechne_rendite(100))

# Aufgabe 1:
class Tier:
    def __init__(self, name):
        self.name = name

    def schlafen(self):
        print(f"{self.name} schläft gerade.")

class Hund(Tier):
    def bellen(self):
        print("Wuff")
    
class Katze(Tier):
    def miauen(self):
        print("Miau")

bello = Hund("bello")
bello.schlafen()
bello.bellen()
print(bello.name)


katze = Katze("katze")
katze.schlafen()
katze.miauen()


class Fahrzeug:

    def __init__(self, gewicht, anzahl_raeder):
        self.gewicht = gewicht
        self.anzahl_raeder = anzahl_raeder

    def __str__(self):
        return f"Ich bin ein Fahrzeug mit {self.anzahl_raeder} Rädern und {self.gewicht} kg schwer"

class Fahrrad(Fahrzeug):
    
    def __init__(self, gewicht):
        super().__init__(gewicht, 2)

    def klingeln(self):
        print("Klingeling")

class Pkw(Fahrzeug):
    def __init__(self, gewicht):
        super().__init__(gewicht, 4)

mein_bike = Fahrrad(20)
print(mein_bike)
mein_bike.klingeln()

mein_auto = Pkw(2000)
print(mein_auto)