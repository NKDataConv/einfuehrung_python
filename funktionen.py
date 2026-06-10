def addition(summand_1, summand_2):
    ergebnis = summand_1 + summand_2
    return ergebnis

# mit typehints
def addition(summand_1: int, summand_2: int) -> int:
    ergebnis = summand_1 + summand_2
    return ergebnis

a = addition(3, 2.312)
print(a)

def bellen():
    print("wuff")

bellen()

def mean(zahlen: list) -> float:
    summe = sum(zahlen)
    durchschnitt = summe / len(zahlen)
    return durchschnitt

ergebnis = mean([1, 2, 3, 4])
print(ergebnis)

# Aufgabe 1:
def produkt(a: float, b: float, c: float) -> float:
    return a * b * c

ergebnis = produkt(a=1, c=3, b=2)
print(ergebnis)

# Aufgabe 2
def min_max(zahlen: list) -> dict:
    minimum = min(zahlen)
    maximum = max(zahlen)
    min_max_dict = {"Minimum": minimum, "Maximum": maximum}
    return min_max_dict

def min_max(zahlen: list) -> dict:
    minimum = min(zahlen)
    maximum = max(zahlen)
    return {"Minimum": minimum, "Maximum": maximum}

ergebnis = max([3,5,2,7,1, 100, -131])
print(ergebnis)

# Aufgabe 3
vermögen = {"Vermögen": 700, "Zinsen": 5, "Jahre": 10}

def berechne_endvermögen(vermögen):
    p = vermögen["Vermögen"]
    r = vermögen["Zinsen"] / 100
    t = vermögen["Jahre"]
    endvermögen = p * (1+r)**t
    return endvermögen

endvermögen = berechne_endvermögen(vermögen)
print(f"Das Endvermögen nach 10 Jahren beträgt: {endvermögen:.2f} €")

def vermögensrechnung(vermögen, zinssatz, jahre):
    ergebnis = vermögen * (1+zinssatz) ** jahre
    return ergebnis

print(f"{round(vermögensrechnung(2000, 0.06, 20), 2)} €")

# Aufgabe 1
zahlen_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def filtere_gerade_zahlen(zahlen_liste) -> list:
    neue_zahlen_liste = []
    for zahl in zahlen_liste:
        if zahl % 2 == 0:
            neue_zahlen_liste.append(zahl)
    return neue_zahlen_liste

print(filtere_gerade_zahlen(zahlen_liste))

# Aufgabe 2
text = """Es war einmal ein kleiner Leuchtturm namens Keno. Er stand auf einer winzigen, runden Klippe mitten im tosenden Meer. Keno war nicht so hoch wie die stolzen Prachtbauten auf dem Festland, und seine Lampe war kein gigantisches Scheinwerferlicht, sondern ein warmes, bernsteinfarbenes Glühen.
Die großen Schiffe, die majestätisch am Horizont vorbeizogen, würdigten Keno keines Blickes. Sie orientierten sich an den mächtigen Laserstrahlen der großen Häfen. Manchmal fühlte Keno sich deshalb ein bisschen nutzlos. Er fragte sich, ob es überhaupt jemanden kümmerte, dass er Nacht für Nacht seine kleine Lampe polierte und hell leuchten ließ.
Die Sturmnacht
In einer feuchtkalten Herbstnacht zog ein heftiger Sturm auf. Die Wellen peitschten wie schwarze Berge gegen Kenos Klippe, und der Wind heulte so laut, dass die Fensterscheiben zitterten. Plötzlich fiel auf dem fernen Festland der Strom aus. Die großen, stolzen Leuchttürme wurden schlagartig dunkel.
Keno geriet in Panik. Wenn die Großen erloschen waren, wie sollte er dann gegen diese Finsternis ankommen? Doch er nahm all seinen Mut zusammen, drehte seinen Reflektor so schnell er konnte und schickte sein warmes, bernsteinfarbenes Licht weit hinaus in die tosende Gischt.
Ein kleines Licht rettet Leben
Gegen Mitternacht entdeckte Keno ein winziges Flackern auf dem Wasser. Es war kein stolzer Ozeanriese, sondern ein kleiner Fischerbote, der vom Sturm überrascht worden war. Der Motor war ausgefallen, die Wellen drohten das Boot zu zerschmettern, und die Fischer an Bord hatten jede Orientierung verloren.
Da sahen sie Kenos Licht. Es war nicht blendend hell, aber es war stetig, warm und zeigte ihnen genau, wo die gefährlichen Klippen lagen.
„Dort drüben!“, rief der Kapitän gegen den Wind an. „Haltet euch auf das warme Licht zu!“
Mit letzter Kraft steuerten die Fischer ihr Boot in den Windschatten von Kenos kleiner Klippe. Dort waren sie vor den schlimmsten Wellen geschützt und warteten sicher, bis der Sturm am Morgen nachließ.
Klein, aber goldwert
Als die Sonne am nächsten Tag die Wolken durchbrach, war das Meer wieder friedlich. Die Fischer winkten Keno dankbar zu, bevor sie den Heimweg antraten.
Keno löschte erschöpft, aber glücklich seine Lampe für den Tag. Er hatte verstanden: Man muss nicht der Größte oder der Lauteste sein, um der Welt den Weg zu weisen. Manchmal reicht ein kleines, treues Licht genau zur rechten Zeit."""

def zaehle_woerter(text):
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("\n", " ")
    text = text.replace("?", "")
    text = text.replace("!", "")
    text = text.lower()
    text_als_liste = text.split(" ")

    wort_count = {}
    for wort in text_als_liste:
        if wort in wort_count.keys():
            wort_count[wort] = wort_count[wort] + 1
        else:
            wort_count[wort] = 1
    
    return wort_count

print(zaehle_woerter(text))

# n muss eine natürliche Zahl sein.
def fakultaet(n: int):
    """n muss eine natürliche Zahl sein."""
    if n % 1 != 0:
        print("Falsche Eingabe")
    if n < 1:
        print("Falsche Eingabe")
        return 0
    
    if n == 1:
        return 1
    else:
        return n * fakultaet(n-1)
    
print(fakultaet(10))