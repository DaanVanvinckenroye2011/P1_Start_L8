from sterren_module import *
import random

kleuren = ("red", "orange", "yellow", "lime green", "orchid", "magenta", "dodger blue", "crimson", "chocolate", "navy", "salmon", "green yellow", "teal", "cyan", "aquamarine", "hot pink", "firebrick", "royal blue", "wheat")

while True:
    x = random.randint(-500, 500)
    y = random.randint(-400, 400)
    kleur = random.choice(kleuren)
    # kies een willekeurige kleur

    # geef de juiste variabelen aan de functie teken_ster()
    teken_ster(x, y, kleur)