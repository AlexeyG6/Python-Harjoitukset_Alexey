sukupuoli = input("Anna biologinen sukupoulisi (Mies, Nainen): ")

hemoglobini = float(input("Anna hemoglobiiniarvosi (g/l): "))

if sukupuoli == "Mies":
    if hemoglobini < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemoglobini > 195:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")

elif sukupuoli == "Nainen":
    if hemoglobini < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemoglobini > 175:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")