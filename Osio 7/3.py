

def GalooniLitraksi(galoonit):
    litrat = galoonit * 3.785
    return litrat

while True:
    galoonit = float(input("Anna galoonien määrä: "))
    if galoonit < 0:
        break
    litrat = GalooniLitraksi(galoonit)
    print(f"{galoonit} galoonia on {litrat} litraa.")