"""
- Magic methods

- len(a) = a.__len__()

- Auto Klasse erzeugen
- PS als attribut vergeben
- wenn a1 50PS hat und a2 60PS und a1+a2 rechnet soll direkt 110 ausgegeben werden
- subtraktion und multiplikation soll auf den Auto-objekten möglich sein
- achtung überprüfen ob geegnete objekte addiert, subtrahiert usw. werden
- EQ,LT,GT vergleichsoperationen abbilden
- für alle magicmethods testzeilen angeben



später bei linkedlist:
 __setitem__ __getitem__ __contains__=in operator
with = contextmanager klappt, wenn eine klasse __enter_ und __exit implementiert
iteratoren müssen __iter__ __next__ implementiert next braucht raise Stopiteration
"""

class Auto:
    def __init__(self, ps):
        self.ps = ps

    def __add__(self, other):
        if isinstance(other, Auto):
            return self.ps + other.ps
        else:
            raise TypeError("Man kann nur zwei Autos miteinander addieren")

    def __sub__(self, other):
        if isinstance(other, Auto):
            return self.ps - other.ps
        else:
            raise TypeError("Man kann nur zwei Autos miteinander subtrahieren")

    def __mul__(self, other):
        if isinstance(other, Auto):
            return self.ps * other.ps
        else:
            raise TypeError("Man kann nur zwei Autos miteinander multiplizieren")
        
    def __eq__(self, other):
        return isinstance(other, Auto) and self.ps == other.ps

    def __lt__(self, other):
        return isinstance(other, Auto) and self.ps < other.ps

    def __gt__(self, other):
        return isinstance(other, Auto) and self.ps > other.ps


def main():
    a1 = Auto(150)
    a2 = Auto(200)

    print(a1 + a2)
    print(a1 - a2)
    print(a1 * a2)

    print("Gleiche PS?:")
    print(a1 == a2)

    print("Auto A1 weniger PS als Auto A2?:")
    print(a1 < a2)
    
    print("Auto A1 mehr PS als Auto A2?:")
    print(a1 > a2)



if __name__ == "__main__":
    main()
