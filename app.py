from country_list import get_countries
import random
from ascii import HANGMANPICS
from contry_and_capital_list import countries_and_capitals

countries = get_countries()
capitals = countries_and_capitals()

print("Üdvözöllek az Akasztófa játékban!")

jo_tippek = []
rossz_tippek = []


# nehezseg: 0 -> könnyű, 1 -> közepes, 2 -> nehéz
def jatek(nehezseg):
    jo_tippek.clear()
    rossz_tippek.clear()

    # életek száma
    elet = 7

    match (nehezseg):
        case 0:
            orszag = random.choice(
                [country for country in countries if " " not in country])  # minden ország amiben nincs szóköz
        case 1:
            orszag = random.choice(
                [country for country in countries if " " in country])  # minden ország amiben van szóköz
        case 2:
            elet = 5
            orszag = random.choice(capitals)

    orszag_len = len(orszag)
    ismeretlen = ""
    for i in orszag:
        if i == " ":
            ismeretlen += " "
        elif i != "|":
            ismeretlen += "_"
        else:
            ismeretlen += "|"

    print(f"Az ország hossza: {orszag_len} karakter.")
    print(f"A kitalálandó ország: \n{ismeretlen}")

    while elet > 0:
        tipp = input("Adj meg egy betűt, vagy megoldást: ").strip()

        # Helyes tipp
        if tipp.lower() == orszag.lower():
            print("Gratulálok, kitaláltad az országot! 🎉")

            while True:
                ask = input("Szeretnél még játszani? (Igen/Nem)")
                if ask.lower() == "igen":
                    kezdes()
                elif ask.lower() == "nem":
                    print("Játék vége!")
                    break
                else:
                    print("Ezt nem tudom értelmezni! Igen vagy Nem választ fogadok el csak.")
        # kilépés
        elif tipp.lower() == "quit":
            kilepes = input("- Kilépés -\nBiztos ki akarsz lépni? (igen/nem): ").strip().lower()
            if kilepes == "igen":
                print("Kilépés..")
                exit()
            else:
                print("Játék folytatása...")
                continue
        # Rossz tipp
        elif len(tipp) != 1:
            elet -= 1
            print(HANGMANPICS[6 - elet])
            print(f"Helytelen válasz! ❌")
            print("> Rossz válaszok:", ", ".join(rossz_tippek), "\n> Jó válaszok:", ", ".join(jo_tippek))
            print("> Megmaradt életed:", elet, " 💔")

        # már felhasznált betű
        elif tipp.lower() in jo_tippek or tipp.lower() in rossz_tippek:
            print("Ezt a betűt már próbáltad! ❌")

        # helyes betű
        elif tipp.lower() in orszag.lower():
            jo_tippek.append(tipp.lower())
            print(f"Helyes válasz! ✅>")
            print("> Rossz válaszok:", ", ".join(rossz_tippek), "\n> Jó válaszok:", ", ".join(jo_tippek))

            # megadott betűk kicserélése
            uj_ismeretlen = ""
            for i in range(len(orszag)):
                if orszag[i].lower() == tipp.lower():
                    uj_ismeretlen += orszag[i]
                else:
                    uj_ismeretlen += ismeretlen[i]
            ismeretlen = uj_ismeretlen
            print(ismeretlen)

            # Nincs több ismeretlen betű
            if "_" not in ismeretlen:
                print("Gratulálok, kitaláltad az országot! 🎉")

                while True:
                    ask = input("Szeretnél még játszani? (Igen/Nem)")
                    if ask.lower() == "igen":
                        kezdes()
                    elif ask.lower() == "nem":
                        print("Játék vége!")
                        exit()
                    else:
                        print("Ezt nem tudom értelmezni! Igen vagy Nem választ fogadok el csak.")

        # rossz válasz
        elif tipp.lower() not in orszag.lower():
            rossz_tippek.append(tipp.lower())
            elet -= 1

            print(HANGMANPICS[6 - elet])
            print(f"Helytelen válasz! ❌")
            print("> Rossz válaszok:", ", ".join(rossz_tippek), "\n> Jó válaszok:", ", ".join(jo_tippek))
            print("> Megmaradt életed:", elet, " 💔")

    print(f"Vesztettél! Az ország: {orszag}")

    while True:
        ask = input("Szeretnéd újra megpróbálni? (Igen/Nem) ")
        if ask.lower() == "igen":
            kezdes()
        elif ask.lower() == "nem":
            print("Játék vége!")
            exit()
        else:
            print("Ezt nem tudom értelmezni! Igen vagy Nem választ fogadok el csak.")


# Nehézség kiválasztása
def kezdes():
    while True:
        try:
            jatek_valasztas = int(input("Válassz szintet!\nKönnyű (1)\nKözepes (2)\nNehéz (3)\nVálassz!: "))
            if jatek_valasztas == 1:
                print("Könnyű nehézség kiválasztva! ✅")
                jatek(0)
                break
            elif jatek_valasztas == 2:
                print("Közepes nehézség kiválasztva! ✅")
                jatek(1)
                break
            elif jatek_valasztas == 3:
                print("Nehéz nehézség kiválasztva! ✅")
                jatek(2)
                break
            else:
                print("Helytelen formátum! ❌")
        except ValueError:
            print("Kérlek, számot adj meg! ❌")


kezdes()
