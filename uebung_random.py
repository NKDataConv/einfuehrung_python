import random

# Aufgabe 1a
zufallszahlen = []
for _ in range(0, 10):
    zufallszahlen.append(random.uniform(0, 2))
    zufallszahlen.append(random.random()*2)
print(zufallszahlen)

# Aufgabe 1b
zufallszahlen = []
for _ in range(0, 100000):
    zufallszahlen.append(random.randint(-10, 10))

# Aufgabe 2
import statistics
print(f"Mittelwert: {statistics.mean(zufallszahlen)}")
print(f"Standardabweichung: {statistics.stdev(zufallszahlen)}")
print(f"Median: {statistics.median(zufallszahlen)}")

def wuerfeln():
    return random.randint(1,6)

print(wuerfeln())

def generiere_passwort(anzahl_zeichen: int, sonderzeichen: bool):
    zulaessige_zeichen = ["a", "b", "c", "d"]
    if sonderzeichen:
        zulaessige_zeichen.append(",")
        zulaessige_zeichen.append("!")
        zulaessige_zeichen.append("&")

    passwort = random.choices(zulaessige_zeichen, k=anzahl_zeichen)
    passwort = "".join(passwort)
    return passwort

print(generiere_passwort(10, False))