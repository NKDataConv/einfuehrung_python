my_list = [1, 2, 3]
andere_liste = ["asdf", "ölkj", "poiu", "kahsdf"]
letzte_liste = [True, True, False]

erste_element = my_list[0]
print(erste_element)

zweite_element = my_list[1]
print(zweite_element)

letzte_element = my_list[-1]
print(letzte_element)

laenge_der_liste = len(my_list)
print(laenge_der_liste)

my_list.append(4)
print(my_list)

my_list.append(None)
print(my_list)

del(my_list[0])
print(my_list[0])

print(my_list)
element = my_list.pop(-1)
print(element)
print(my_list)

my_list.append(-1)
my_list.sort()
print(my_list)

for i in my_list:
    print(i)

leere_liste = []
for i in range(1, 100):
    leere_liste.append(i)

# Aufgabe 1:
liste = [3, 4, 3, 2, 3, 5, 3, 4]
summe = 0
for elem in liste:
    # summe = summe + elem
    summe += elem
print("Die Gesamtsumme ist: ", summe)

summe = sum(liste)

# Aufgabe 2 Option 1
maximum = liste[0]
for elem in liste:
    if elem > maximum:
        maximum = elem

# Aufgabe 2 Option 2
liste.sort()
print(liste[-1])

# Aufgabe 2 Option 3
print(max(liste))
