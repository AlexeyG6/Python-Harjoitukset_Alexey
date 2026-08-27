lieviskät = float(input("Anna lieviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

naulat = (lieviskät * 20) + naulat
luodit= (naulat * 32) + luodit
massa = luodit * 13.3

kilot = int(massa // 1000)
grammat = massa % 1000

print("Massa nykymittojen mukaan: ")
print(f"{kilot} kilogrammaa ja {grammat:.2f} grammaa")