from unittest import case


vuodenajat = ["talvi", "kevät", "kesä", "syksy"]
(T,K,KK,S) = vuodenajat
while True:
    kuukaus = int(input("Anna kuukausi (1-12): "))

    if kuukaus < 1 or kuukaus > 12:
        print("Virheellinen kuukausi. Anna luku väliltä 1-12.")
    else:
        break

match kuukaus:
    case 12 | 1 | 2:
        print("Kuukausi kuuluu vuodenaikaan:", T)
    case 3 | 4 | 5:
        print("Kuukausi kuuluu vuodenaikaan:", K)
    case 6 | 7 | 8:
        print("Kuukausi kuuluu vuodenaikaan:", KK)
    case 9 | 10 | 11:
        print("Kuukausi kuuluu vuodenaikaan:", S)