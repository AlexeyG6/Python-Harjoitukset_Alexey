luku = int(input("Anna luku:"))
l = 0
13

for i in range(1, luku + 1):
    if luku % i == 0:
        l += 1

if l == 2:
    print(f"{luku} on alkuluku.")
else:
    print(f"{luku} ei ole alkuluku.")