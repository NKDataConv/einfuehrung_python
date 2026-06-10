import math
from math import sqrt

print(math.e)
print(math.sqrt(2))
print(math.sin(2))
print(math.pi)
print(sqrt(2))

# Aufgabe 1:
y = math.sin(2) / (math.cos(3)**2)


# Option 1 
summe = 0
for i in range(1, 101):
    summe = summe + math.sin(i)
print(summe)

# Option 2
print(sum(math.sin(i) for i in range(1,101)))

# Option 3
sinuse = []
for i in range(1, 101):
    sinuse.append(math.sin(i))
print(math.fsum(sinuse))

# Aufgabe 2
def berechnung(y):
    if y <= 0:
        return math.e ** y * math.sqrt(2)
    else:
        return math.e ** y * math.sqrt(3)
    
print(berechnung(2))