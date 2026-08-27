

def GalooniLitraksi(galoonit):
    litrat = galoonit * 3.785
    return litrat

while True:
    galoonit = input("Anna galoonien määrä: ")
    if galoonit == "":
        break
    galoonit = float(galoonit)
    litrat = GalooniLitraksi(galoonit)
    print(f"{galoonit} galoonia on {litrat} litraa.")