
import random

def HeitaNoppaa(noppa):
    while True:
        yritys =random.randint(1, noppa)
        print(f"{yritys}")
        if yritys == noppa:
            break

noppa = int(input("Tahkojen määrä? "))
HeitaNoppaa(noppa)