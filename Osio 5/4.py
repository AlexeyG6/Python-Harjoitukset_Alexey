import random


luku = random.randint(1, 10)
while True:
    arvaus = int(input("Arvaa luku väliltä 1-10: "))
    if arvaus == luku:
        break
print("Arvasit oikein!")