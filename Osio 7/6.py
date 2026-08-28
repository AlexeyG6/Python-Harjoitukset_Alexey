

def Pizzankoko(halkaisija):
    return (halkaisija / 2) ** 2 * 3.14
    
    


pizza_1 = float(input("Ensimmäisen pizzan halkaisija cm: "))
pizza_2 = float(input("Toisen pizzan halkaisija cm: "))
koko_1 = float(input("Ensimmäisen hinta: "))
koko_2 = float(input("Toisen pizzan hinta: "))
piz_1_pinta = Pizzankoko(pizza_1)
piz_2_pinta = Pizzankoko(pizza_2)

piz_1_pinta_per_hinta = piz_1_pinta / koko_1
piz_2_pinta_per_hinta = piz_2_pinta / koko_2

print("Ensimmäisen pizzan hinta per pinta-ala: ", piz_1_pinta_per_hinta)
print("Toisen pizzan hinta per pinta-ala: ", piz_2_pinta_per_hinta)

if piz_1_pinta_per_hinta > piz_2_pinta_per_hinta:
    print("Ensimmäinen pizza on parempi hinta-laatusuhteeltaan.")
else:
    print("Toinen pizza on parempi hinta-laatusuhteeltaan.")
