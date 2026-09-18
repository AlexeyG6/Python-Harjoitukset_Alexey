
import random


def HeitaNoppaa():
    while True:
        yritys =random.randint(1, 6)
        print(f"{yritys}")
        heitto += 1
        if yritys == 6:
            print(heitto, "heittoa")
            break

heitto = 0
HeitaNoppaa()
        