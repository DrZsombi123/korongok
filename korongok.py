korongok = []
while True:
    try:
        sorok_szama = input("Adja meg a sor számát.")
        if sorok_szama == "":
            break
        sorok_szama = int(sorok_szama)
        if sorok_szama < 1 or sorok_szama > 8:
            print("A sorok számnak 1 és 8 között kell lennie.")
            continue

        oszlopokszama = input("Adja meg az oszlopok számát.")
        if oszlopokszama == "":
            break
        oszlopokszama=int(oszlopokszama)
        if oszlopokszama < 1 or oszlopokszama > 8:
            print("Az oszlopok száma 1 és 8 között kell lennie.")
            continue
        korongpoz = (f"{sorok_szama}K{oszlopokszama}")
        if korongpoz in korongok:
            korongok.remove(korongpoz)
            print("Eltávolítottad a korongpoz a listábol.")
        else:
            korongok.append(korongpoz)
            print("Sikeresen hozzáadtad a listához.")
    except ValueError:
        print("Csak számot adhatsz meg.")

print(korongok)
