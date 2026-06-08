# # for - Schleife

# for i in [1, 2, 3]:
#     print(i)

# for person in ["a", "b", "c"]:
#     print("Hallo ", person)
# print("Hallo ", person)

# my_array = [1, 2, 3]
# for i in my_array:
#     print(i)

# # while - Schleifen
# laenge_des_array = len(my_array)
# while laenge_des_array>0:
#     print(laenge_des_array)
#     laenge_des_array = laenge_des_array - 1

# for counter in [1, 2, 3]:
#     for j in [4, 5, 6]:
#         print(counter, j)

# for i in ["a", "b", "c"]:
#     print(i)

# i = True

# for i in range(0, 10):
#     print(i)

# Aufgabe 1 a, Option 1:
for i in range(1, 15):
    print(i*2)

# Aufgabe 1 a, Option 2:
for i in range(1, 29):
    if i % 2 == 0:
        print(i)

# Aufgabe 1 a, Option 3:
for i in range(2, 29, 2):
    print(i)

# Aufgabe 1 a, Option 4:
n = 0
while n <= 28:
    if n % 2 == 0:
        print(n)
    n = n + 1

# Aufgabe 1 b
for i in range(1, 11):
    print(i**2)

for n in range(1,15):
    quadrat = n*n
    if quadrat > 100:
        break
    print(quadrat)

i = 1
while i <=10:
    print(i*i)
    i += 1

# Aufgabe 1 c
for i in range(1, 10):
    print(2**i)

for i in range(1, 513):
    if i >= 0 and (i & (i-1)) == 0:
        print(i)

for i in range(1, 10):
    print(2**i)

# Aufgabe 2:
zahl = 5
produkt = 1
for i in range(1, zahl+1):
    produkt = produkt * i
print(produkt)