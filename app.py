from country_list import get_countries
import random

countries = get_countries()

print("Üdvözöllek az akasztófa játékban!")

orszag_index = random.randint(0, 182)
orszag = countries[orszag_index]
print(orszag)
print(f"A kitalálandó ország: \n{orszag * "_ "}")

elet = 7
tipp = input("Adj meg egy betűt! ")
if tipp == orszag:
    print("Gratulálok, nyertél!")





def kezdes():

    while True:
        jatek_valasztas = int(input("Válassz szintet!\nKönnyű (1)\nKözepes (2)\nNehéz (3)\nVálassz!: "))
        if jatek_valasztas == 1:
            print("Könnyű nehézség kiválasztva! ✅")
            easy()
        elif jatek_valasztas == 2:
            print("Közepes nehézség kiválasztva! ✅")
            medium()
        elif jatek_valasztas == 3:
            print("Nehéz nehézség kiválasztva! ✅")
            hard()
        else:
            print("Helytelen formátum! ❌")

kezdes()
