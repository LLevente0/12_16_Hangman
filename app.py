from country_list import get_countries
import random

countries = get_countries()

print("Üdvözöllek az Akasztófa játékban!")

orszag_index = random.randint(0, 182)  # 182 vagy 183?
orszag = countries[orszag_index]
orszag_len = len(orszag)
ismeretlen = ""
jo_tippek = []
rossz_tippek = []

for i in orszag:

    if i == " ":
        ismeretlen += "   "
    else:
        ismeretlen += "_ "


def easy():
    life = 7

    print(f"Az ország: {orszag}")
    print(f"Hossz: {orszag_len}")
    print(f"A kitalálandó ország: \n{ismeretlen}")

    while life > 0:

        tipp = input("Adj meg egy betűt, vagy megoldást: ")

        if tipp.lower() == orszag.lower():
            print("Gratulálok, nyertél! 🏆")
            break

        elif tipp.lower() in jo_tippek or rossz_tippek:
            print("Ezt a betűt már próbáltad! ❌")

        elif tipp == "quit":
            quit = input("- Kilépés -\nBiztos ki akarsz lépni? (igen/nem)")

            if quit == "igen":
                break

            elif quit == "nem":
                continue

        elif tipp.lower() in orszag.lower():
            jo_tippek.append(tipp.lower())
            print(f"Helyes válasz! ✅\n> Rossz válaszok: {rossz_tippek} \n> Jó válaszok: {jo_tippek}")
            # replace?
            # megkeresni hol vannak azok a betűk, ott kicserélni pontosan, ha van többet is akár
            print(ismeretlen)

        elif tipp.lower() not in orszag.lower():
            rossz_tippek.append(tipp.lower())
            life -= 1
            print(f"Helytelen válasz! ❌\n> Rossz válaszok: {rossz_tippek}\n> Jó válaszok: {jo_tippek}")
            print("Megmaradt életed:", life, " 💔")


def kezdes():
    while True:
        jatek_valasztas = int(input("Válassz szintet!\nKönnyű (1)\nKözepes (2)\nNehéz (3)\nVálassz!: "))

        if jatek_valasztas == 1:
            print("Könnyű nehézség kiválasztva! ✅")
            easy()

        elif jatek_valasztas == 2:
            print("Közepes nehézség kiválasztva! ✅")


        elif jatek_valasztas == 3:
            print("Nehéz nehézség kiválasztva! ✅")

        else:
            print("Helytelen formátum! ❌")

kezdes()