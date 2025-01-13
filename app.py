from country_list import get_countries
import random

countries = get_countries()

print("Üdvözöllek az Akasztófa játékban!")

orszag_index = random.randint(0, len(countries) - 1)
orszag = countries[orszag_index]
orszag_len = len(orszag)
ismeretlen = ""

for i in orszag:
    if i == " ":
        ismeretlen += "   "
    else:
        ismeretlen += "_ "

jo_tippek = []
rossz_tippek = []


def easy():
    life = 7
    global ismeretlen

    print(f"Az ország hossza: {orszag_len} karakter.")
    print(f"A kitalálandó ország: \n{ismeretlen}")

    while life > 0:
        tipp = input("Adj meg egy betűt, vagy megoldást: ").strip()

        if tipp.lower() == orszag.lower():
            print("Gratulálok, nyertél! 🏆")
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

            new_ismeretlen = ""
            for i in range(len(orszag)):
                if orszag[i].lower() == tipp.lower():
                    new_ismeretlen += orszag[i] + " "
                else:
                    new_ismeretlen += ismeretlen[i * 2] + " "
            ismeretlen = new_ismeretlen
            print(ismeretlen)

            if "_" not in ismeretlen:
                print("Gratulálok, kitaláltad az országot! 🎉")
                break

        else:
            rossz_tippek.append(tipp.lower())
            life -= 1
            print(f"Helytelen válasz! ❌\n> Rossz válaszok: {rossz_tippek}\n> Jó válaszok: {jo_tippek}")
            print("Megmaradt életed:", life, " 💔")

            if life == 0:
                print(f"Vesztettél! Az ország: {orszag}")


def kezdes():
    while True:
        try:
            jatek_valasztas = int(input("Válassz szintet!\nKönnyű (1)\nKözepes (2)\nNehéz (3)\nVálassz!: "))
            if jatek_valasztas == 1:
                print("Könnyű nehézség kiválasztva! ✅")
                easy()
                break  # End after the game is finished
            elif jatek_valasztas == 2:
                print("Közepes nehézség kiválasztva! ✅")
                # Add medium difficulty logic here
            elif jatek_valasztas == 3:
                print("Nehéz nehézség kiválasztva! ✅")
                # Add hard difficulty logic here
            else:
                print("Helytelen formátum! ❌")
        except ValueError:
            print("Kérlek, számot adj meg! ❌")


kezdes()
