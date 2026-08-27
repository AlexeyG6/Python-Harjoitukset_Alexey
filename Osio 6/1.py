import random

määrä = int(input("Syötä arvottavien kuutioiden määrä: "))
i = 0
summa = 0

for i in range(määrä):
    Kuutio_luku = random.randint(1, 6)
    summa += Kuutio_luku
    i += 1

print(f"Arvottujen kuutioiden summa: {summa}")
