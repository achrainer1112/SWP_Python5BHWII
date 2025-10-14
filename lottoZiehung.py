import random

def ziehung(statistik, zahlenbereich, anzahl_ziehungen):
    zahlen = list(range(1, zahlenbereich + 1))
    for _ in range(anzahl_ziehungen):
        random_index = random.randrange(0, len(zahlen))
        element = zahlen.pop(random_index)
        zahlen.append(element)
        statistik[element] += 1

def main():
    zahlenbereich = 45
    anzahl_ziehungen = 6
    durchlaeufe = 1000
    statistik = {i: 0 for i in range(1, zahlenbereich + 1)}

    for _ in range(durchlaeufe):
        ziehung(statistik, zahlenbereich, anzahl_ziehungen)

    print(statistik)

if __name__ == "__main__":
    main()

