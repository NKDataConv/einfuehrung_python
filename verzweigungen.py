if -1>0: 
    print("positive Zahl")
else:
    print("negative Zahl")

# Aufgabe 1
zahl = 4
bedingung = zahl % 2 == 0
if bedingung:
    print("Gerade")
else: 
    print("Ungerade")

# Aufgabe 2:
zahl = -3
if zahl > 0:
    print("positiv")
elif zahl < 0:
    print("negativ")
else:
    print("null")

# Aufgabe 3 Option 1
jahr = 200
if jahr % 4 == 0:
    if jahr % 400 == 0:
        print("Schaltjahr")
    elif jahr % 100 == 0:
        print("Kein Schaltjahr")
    else:
        print("Schaltjahr")
else:
    print("Kein Schaltjahr")


# Aufgabe 3 Option 2
jahr = 200
bedingung_4 = jahr % 4 == 0
bedingung_100 = jahr % 100 == 0
bedingung_400 = jahr % 400 == 0
if bedingung_4 and (not bedingung_100) or bedingung_400:
    print("Schaltjahr")
else:
    print("Kein Schaltjahr")

schaltjahr = 2008
if (schaltjahr % 4 == 0 and schaltjahr % 100 != 0) or (schaltjahr % 400 == 0):
    print(schaltjahr, "! ist ein Schaltjahr")
else:
    print(schaltjahr, "ist kein Schaltjahr")