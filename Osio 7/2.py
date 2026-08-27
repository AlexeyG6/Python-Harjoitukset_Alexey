
import random

noppa = int(input("Tahkojen määrä? "))

def HeitaNoppaa():
    while True:
        yritys =random.randint(1, noppa)
        print(f"{yritys}")
        if yritys == noppa:
            break

HeitaNoppaa()
        