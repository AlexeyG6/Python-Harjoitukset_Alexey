#Tehtävä 1.2: Parilliset luvut ja summa
#Kirjoita ohjelma, joka pyytää käyttäjältä positiivisen kokonaisluvun $N$. Ohjelma tulostaa kaikki parilliset kokonaisluvut väliltä $1 \dots N$ sekä laskee näiden parillisten lukujen summan.

N = int(input("Anna kokonais N:"))
i = 0
while i <= N:
    print (i)
    i += 2