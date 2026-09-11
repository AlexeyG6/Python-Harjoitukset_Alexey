import random

i = 0
N = int(input("Syötä arvottavien pisteiden määrä: "))
n = 0

while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        n += 1
    i += 1
pi = 4 * n / N

print(f"Piin likiarvo: {pi}")