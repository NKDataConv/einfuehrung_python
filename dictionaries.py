woerterbuch = {"cat": "Katze", "gato": "Katze", "dog": "Hund"}
schalten = {"oben": True, "unten": False}
zahlen = {1: "ungerade", 2: "gerade"}
konstanten = {"pi": 3.14, "g": 9.81, "wurzel_2": 1.41, "elektronen_ladung": -1.602*10**(-19)}

print(woerterbuch["cat"])
print(woerterbuch["dog"])

person_1 = {"name": "Peter", "alter": 21}
person_2 = {"name": "Sabine", "alter": 23}

person_1 = ["Peter", 21]
person_2 = ["Sabine", 23]

print(len(woerterbuch))
print(woerterbuch.keys())
print(woerterbuch.values())

for k, v in woerterbuch.items():
    print(k)

for k, v in woerterbuch.items():
    print(v)

for v in woerterbuch.values():
    print(v)

elem = woerterbuch.pop("cat")
print(elem)
print(woerterbuch)

woerterbuch.update({"dog": "asdf"})
print(woerterbuch)

# Aufgabe 1
personen = {"Peter": 14, "Maria": 19, "Florian": 17}

print(personen["Florian"])
print(personen.keys())
print(list(personen.keys())[1])

for name, alter in personen.items():
    if name == "Peter":
        print(name, alter)

# Aufgabe 2
# for name, alter in personen.items():
#     personen[name] = alter+1
# print(personen)

nicht_volljaehrig = []
for name, alter in personen.items():
    if alter < 18:
        nicht_volljaehrig.append(name)
print(nicht_volljaehrig)