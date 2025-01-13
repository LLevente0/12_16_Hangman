from country_list import get_countries
import random
from ascii import HANGMANPICS
from contry_and_capital_list import countries_and_capitals

countries = get_countries()
capitals = countries_and_capitals()

print("Üdvözöllek az Akasztófa játékban!")

orszag_index = random.randint(0, len(countries) - 1)
orszag = countries[orszag_index]
orszag_len = len(orszag)
fovaros_index = random.randint(0, len(capitals) - 1)
fovaros = capitals[fovaros_index]
fovaros_len = len(fovaros)
ismeretlen = ""

for i in orszag:
    if i == " ":
        ismeretlen += "   "
    else:
        ismeretlen += "_ "

jo_tippek = []
rossz_tippek = []


def easy():
    elet = 7
    global ismeretlen

    print(orszag)
    print(f"Az ország hossza: {orszag_len} karakter.")
    print(f"A kitalálandó ország: \n{ismeretlen}")

    while elet > 0:
        tipp = input("Adj meg egy betűt, vagy megoldást: ").strip()

        if tipp.lower() == orszag.lower():
            print("Gratulálok, kitaláltad az országot! 🎉")
            break

        elif tipp.lower() in jo_tippek or tipp.lower() in rossz_tippek:
            print("Ezt a betűt már próbáltad! ❌")

        elif tipp.lower() == "quit":
            kilepes = input("- Kilépés -\nBiztos ki akarsz lépni? (igen/nem): ").strip().lower()
            if kilepes == "igen":
                print("Sikeres kilépés! 👋")
                break
            else:
                print("Játék folytatása...")
                continue

        elif tipp.lower() in orszag.lower():
            jo_tippek.append(tipp.lower())
            print(f"Helyes válasz! ✅\n> Rossz válaszok: {rossz_tippek} \n> Jó válaszok: {jo_tippek}")

            uj_ismeretlen = ""
            for i in range(len(orszag)):
                if orszag[i].lower() == tipp.lower():
                    uj_ismeretlen += orszag[i] + " "
                else:
                    uj_ismeretlen += ismeretlen[i * 2] + " "
            ismeretlen = uj_ismeretlen
            print(ismeretlen)

            if "_" not in ismeretlen:
                print("Gratulálok, kitaláltad az országot! 🎉")
                break

        else:
            rossz_tippek.append(tipp.lower())
            elet -= 1
            print(f"Helytelen válasz! ❌\n> Rossz válaszok: {rossz_tippek}\n> Jó válaszok: {jo_tippek}")
            print("Megmaradt életed:", elet, " 💔")

            if elet == 0:
                print(f"Vesztettél! Az ország: {orszag}")

def hard():
    elet = 5
    global ismeretlen

    print(orszag)
    print(f"Az ország hossza: {orszag_len} karakter.")
    print(f"A kitalálandó ország: \n{ismeretlen}")

    while elet > 0:
        tipp = input("Adj meg egy betűt, vagy megoldást: ").strip()

        if tipp.lower() == orszag.lower():
            print("Gratulálok, kitaláltad az országot! 🎉")
            break

        elif tipp.lower() in jo_tippek or tipp.lower() in rossz_tippek:
            print("Ezt a betűt már próbáltad! ❌")

        elif tipp.lower() == "quit":
            kilepes = input("- Kilépés -\nBiztos ki akarsz lépni? (igen/nem): ").strip().lower()
            if kilepes == "igen":
                print("Sikeres kilépés! 👋")
                break
            else:
                print("Játék folytatása...")
                continue

        elif tipp.lower() in orszag.lower():
            jo_tippek.append(tipp.lower())
            print(f"Helyes válasz! ✅\n> Rossz válaszok: {rossz_tippek} \n> Jó válaszok: {jo_tippek}")

            uj_ismeretlen = ""
            for i in range(len(orszag)):
                if orszag[i].lower() == tipp.lower():
                    uj_ismeretlen += orszag[i] + " "
                else:
                    uj_ismeretlen += ismeretlen[i * 2] + " "
            ismeretlen = uj_ismeretlen
            print(ismeretlen)

            if "_" not in ismeretlen:
                print("Gratulálok, kitaláltad az országot! 🎉")
                break

        else:
            rossz_tippek.append(tipp.lower())
            elet -= 1
            print(f"Helytelen válasz! ❌\n> Rossz válaszok: {rossz_tippek}\n> Jó válaszok: {jo_tippek}")
            print("Megmaradt életed:", elet, " 💔")

            if elet == 0:
                print(f"Vesztettél! Az ország: {orszag}")

def kezdes():
    while True:
        try:
            jatek_valasztas = int(input("Válassz szintet!\nKönnyű (1)\nKözepes (2)\nNehéz (3)\nVálassz!: "))
            if jatek_valasztas == 1:
                print("Könnyű nehézség kiválasztva! ✅")
                easy()
                break
            elif jatek_valasztas == 2:
                print("Közepes nehézség kiválasztva! ✅")
            elif jatek_valasztas == 3:
                print("Nehéz nehézség kiválasztva! ✅")
                hard()
                break
            else:
                print("Helytelen formátum! ❌")
        except ValueError:
            print("Kérlek, számot adj meg! ❌")


kezdes()
