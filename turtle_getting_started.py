import turtle

s = turtle.getscreen()
t = turtle.Turtle()

def quadrat(laenge):
    for _ in range(4):
        t.right(90)
        t.forward(laenge)

# quadrat(10)

laengen_liste = [10, 20, 40, 60]
for laenge in laengen_liste:
    quadrat(laenge)


turtle.done()