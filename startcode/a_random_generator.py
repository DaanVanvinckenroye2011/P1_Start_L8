
import random

first_name = ["Ultra", "Bombo", "skinny","Super", "ABC", "Skibidi", "Blooper",]
second_name = ["Daan", "007", "clat", "Mootje", "Stokbrood", "Banana", "Kilian", "alfabet"]


for i in range (10):

    gekozen_name = random.choice(first_name)
    Twee_gekozen_name = random.choice(second_name)

    print("Jouw user-name is " + gekozen_name + " " + Twee_gekozen_name)