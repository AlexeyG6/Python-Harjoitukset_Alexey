#Tehtävä 1.1: Lämpötilamuunnin
#Kirjoita ohjelma, joka kysyy käyttäjältä lämpötilan Celsius-asteina (liukulukuna) ja muuntaa sen Fahrenheit-asteiksi kaavalla:

celsius = float(input("Anna lämpötila (C): "))
fahrenheit = celsius * 1.8 + 32

print(f"{celsius} Celsius-astetta on {fahrenheit} Fahrenheit-astetta")