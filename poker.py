import random


def deckErzeugen():
    # Farbe: 0 = Herz  |  1 = Karo  |  2 = Pik  |  3 = Kreuz
    # Wert: 2-10 = Zahlenkarten  |  11 = Bube (J)  |  12 = Dame (Q)  |  13 = König (K)  |  14 = Ass (A)
    deck = [(farbe, wert) for farbe in range(4) for wert in range(2, 15)]
    return deck


def ziehung(deck, anzahlKarten):
    return random.sample(deck, anzahlKarten)


# Kombinationen

def hatPaar(gezogeneKarten):
    haeufigkeiten = zaehleHaeufigkeiten(gezogeneKarten)
    if 2 in haeufigkeiten.values():
        return True
    else:
        return False


def hatZweiPaare(gezogeneKarten):
    haeufigkeiten = zaehleHaeufigkeiten(gezogeneKarten)
    if list(haeufigkeiten.values()).count(2) == 2:
        return True
    else:
        return False


def hatDrilling(gezogeneKarten):
    haeufigkeiten = zaehleHaeufigkeiten(gezogeneKarten)
    if 3 in haeufigkeiten.values():
        return True
    else:
        return False


def hatStrasse(gezogeneKarten):
    werte = werteSortieren(gezogeneKarten)

    # Normaler Fall: aufeinanderfolgende Werte prüfen
    ist_strasse = True
    for i in range(1, len(werte)):
        if (werte[i] - 1) != werte[i - 1]:
            ist_strasse = False
            break

    if ist_strasse:
        return True

    # Sonderfall: Ass als niedrigste Karte (A-2-3-4-5)
    if 14 in werte:
        if werte == [2, 3, 4, 5, 14]:
            return True

    return False


def hatFlush(gezogeneKarten):
    farben = farbenExtrahieren(gezogeneKarten)
    for i in range(1, len(farben)):
        if farben[i] != farben[i - 1]:
            return False
    return True


def hatFullHouse(gezogeneKarten):
    if (hatPaar(gezogeneKarten) and hatDrilling(gezogeneKarten)):
        return True
    else:
        return False


def hatVierling(gezogeneKarten):
    haeufigkeiten = zaehleHaeufigkeiten(gezogeneKarten)
    if 4 in haeufigkeiten.values():
        return True
    else:
        return False


def hatStraigthFlush(gezogeneKarten):
    if (hatFlush(gezogeneKarten) and hatStrasse(gezogeneKarten)):
        return True
    else:
        return False


def hatRoyalFlush(gezogeneKarten):
    if (hatStraigthFlush(gezogeneKarten) and werteSortieren(gezogeneKarten)[0] == 10):
        return True
    else:
        return False


# Hilfsfunktionen

def farbenExtrahieren(gezogeneKarten):
    return [karte[0] for karte in gezogeneKarten]


def werteExtrahieren(gezogeneKarten):
    return [karte[1] for karte in gezogeneKarten]


def werteSortieren(gezogeneKarten):
    werte = werteExtrahieren(gezogeneKarten)
    werte.sort()
    return werte


def zaehleHaeufigkeiten(gezogeneKarten):
    haeufigkeiten = {}
    werte = werteExtrahieren(gezogeneKarten)
    for wert in werte:
        if (wert in haeufigkeiten):
            haeufigkeiten[wert] += 1
        else:
            haeufigkeiten[wert] = 1
    return haeufigkeiten


def auswertung(gezogeneKarten, kombinationen):
    if (hatRoyalFlush(gezogeneKarten)):
        kombinationen["Royal Flush"] += 1
    elif hatStraigthFlush(gezogeneKarten):
        kombinationen["Straight Flush"] += 1
    elif hatVierling(gezogeneKarten):
        kombinationen["Vierling"] += 1
    elif hatFullHouse(gezogeneKarten):
        kombinationen["Full House"] += 1
    elif hatFlush(gezogeneKarten):
        kombinationen["Flush"] += 1
    elif hatStrasse(gezogeneKarten):
        kombinationen["Strasse"] += 1
    elif hatDrilling(gezogeneKarten):
        kombinationen["Drilling"] += 1
    elif hatZweiPaare(gezogeneKarten):
        kombinationen["Zwei Paare"] += 1
    elif hatPaar(gezogeneKarten):
        kombinationen["Paar"] += 1


def analyse(kombinationen, durchlaeufe):
    print("Wahrscheinlichkeiten:")
    for karte in kombinationen:
        wert = kombinationen[karte]
        print(karte + ": " + str(round((wert / durchlaeufe) * 100, 3)) + "%")


def main():
    kombinationen = {
        "Royal Flush": 0,
        "Straight Flush": 0,
        "Vierling": 0,
        "Full House": 0,
        "Flush": 0,
        "Strasse": 0,
        "Drilling": 0,
        "Zwei Paare": 0,
        "Paar": 0,
    }

    durchlaeufe = 1000000
    deck = deckErzeugen()

    for i in range(durchlaeufe):
        gezogeneKarten = ziehung(deck, 5)
        auswertung(gezogeneKarten, kombinationen)

    print(kombinationen)
    analyse(kombinationen, durchlaeufe)


if __name__ == "__main__":
    main()
