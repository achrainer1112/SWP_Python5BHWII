"""
names = ["Anna", "Bernd", "Claudia", "Dirk", "Eva"]
ages = [23, 17, 34, 15, 29]
scores = [88, 92, 75, 64, 91]

Erzeuge aus diesen Listen eine gefilterte Liste von Personen, die folgende Bedingungen erfüllt:

Alter ≥ 18 und Score ≥ 80

müssen verwendet werden:

zip – kombiniere die drei Listen so, dass jeder Eintrag ein Tupel (name, age, score) ist.

filter + lambda – filtere alle Personen heraus, die beide Bedingungen erfüllen.

map + lambda – forme jedes Tupel in ein Dictionary der Form
{"name": ..., "age": ..., "score": ...} um.

{"name": "Anna", "age": 23, "score": 88}
"""



def main():
    names = ["Anna", "Bernd", "Claudia", "Dirk", "Eva"]
    ages = [23, 17, 34, 15, 29]
    scores = [88, 92, 75, 64, 91]

    kombiniert = list(zip(names, ages, scores))

    gefiltert = list(filter(lambda person: person[1]>=18 and person[2]>=80, kombiniert))

    umgewandelt = list(map(lambda person: {"Name": person[0], "Age":person[1], "Score":person[2]},gefiltert))


    print(gefiltert)

    print(umgewandelt)




if __name__ == '__main__':
    main()
