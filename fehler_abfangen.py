try:
    # a = 1 / 0
    a = [1, 2, 3]
    print(a[4])
    print("Läuft")

except IndexError as e:
    print("Fehlerfall")
    print(e)
