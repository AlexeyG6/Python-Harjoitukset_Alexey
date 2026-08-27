while True:
    tuuma = float(input("Anna tuumien määrä: "))
    if tuuma < 0:
        print("Tuumien määrä ei voi olla negatiivinen.")
        break
    senttimetri = tuuma * 2.54
    print(f"{tuuma} tuumaa on {senttimetri} senttimetriä.")
