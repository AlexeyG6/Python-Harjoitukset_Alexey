import random

sisäällä = 0
i = 0
määrä = int(input("Syötä arvottavien pisteiden määrä: "))

while i < määrä:
    x = random.randint(-1, 1)
    y = random.randint(-1, 1)

    if x**2 + y**2 < 1:
        sisäällä += 1
    i += 1

print(f"Piin arvio: {4 * sisäällä / määrä}")