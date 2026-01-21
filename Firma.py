from typing import List, Optional

class Person:
    def __init__(self, name: str, geschlecht: str):
        self._name = name
        self._geschlecht = geschlecht.lower()

    def name(self):
        return self._name

    def geschlecht(self):
        return self._geschlecht

    def __str__(self):
        return f"{self._name} ({'Mann' if self._geschlecht == 'm' else 'Frau'})"


class Mitarbeiter(Person):
    def __init__(self, name: str, geschlecht: str, abteilung: 'Abteilung'):
        super().__init__(name, geschlecht)
        self._abteilung = abteilung
        abteilung.add_mitarbeiter(self)

    def abteilung(self):
        return self._abteilung

    def __str__(self):
        return f"{self.name}, Mitarbeiter in {self.abteilung.name}"


class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name: str, geschlecht: str, abteilung: 'Abteilung'):
        super().__init__(name, geschlecht, abteilung)
        abteilung.set_leiter(self)

    def __str__(self):
        return f"{self.name}, Abteilungsleiter von {self.abteilung.name}"


class Abteilung:
    def __init__(self, name: str):
        self._name = name
        self._mitarbeiter: List[Mitarbeiter] = []
        self._leiter: Optional[Abteilungsleiter] = None

    def name(self):
        return self._name

    def mitarbeiter(self):
        return self._mitarbeiter

    def leiter(self):
        return self._leiter

    def add_mitarbeiter(self, mitarbeiter: Mitarbeiter):
        if mitarbeiter not in self._mitarbeiter:
            self._mitarbeiter.append(mitarbeiter)

    def set_leiter(self, leiter: Abteilungsleiter):
        if self._leiter is not None:
            raise ValueError(f"{self._name} hat bereits einen Leiter")
        self._leiter = leiter

    def mitarbeiterzahl(self):
        return len(self._mitarbeiter)


class Firma:
    def __init__(self, name: str):
        self._name = name
        self._abteilungen: List[Abteilung] = []

    def abteilungen(self):
        return self._abteilungen

    def add_abteilung(self, abteilung: Abteilung):
        if abteilung not in self._abteilungen:
            self._abteilungen.append(abteilung)

    def mitarbeiter_anzahl(self):
        return sum(len(a.mitarbeiter) for a in self._abteilungen)

    def abteilungsleiter_anzahl(self):
        return sum(1 for a in self._abteilungen if a.leiter is not None)

    def abteilungsanzahl(self):
        return len(self._abteilungen)

    def abteilung_groesste_mitarbeiterzahl(self):
        if not self._abteilungen:
            return None
        return max(self._abteilungen, key=lambda a: a.mitarbeiterzahl())

    def prozent_frauen_maenner(self):
        frauen = 0
        maenner = 0
        for abteilung in self._abteilungen:
            for mitarbeiter in abteilung.mitarbeiter:
                if mitarbeiter.geschlecht == 'w':
                    frauen += 1
                else:
                    maenner += 1
        gesamt = frauen + maenner
        if gesamt == 0:
            return {"Frauen": 0, "Männer": 0}
        return {"Frauen": round(frauen / gesamt * 100, 1), "Männer": round(maenner / gesamt * 100, 1)}


def main():
    firma = Firma("Tech AG")
    
    it = Abteilung("IT")
    hr = Abteilung("HR")
    vertrieb = Abteilung("Vertrieb")
    
    firma.add_abteilung(it)
    firma.add_abteilung(hr)
    firma.add_abteilung(vertrieb)
    
    Abteilungsleiter("Alice", "w", it)
    Abteilungsleiter("Bob", "m", hr)
    Abteilungsleiter("Clara", "w", vertrieb)
    
    Mitarbeiter("David", "m", it)
    Mitarbeiter("Eva", "w", it)
    Mitarbeiter("Frank", "m", hr)
    Mitarbeiter("Gina", "w", vertrieb)
    Mitarbeiter("Hugo", "m", vertrieb)
    
    print(f"Firma {firma._name}")
    print(f"Anzahl Abteilungen: {firma.abteilungsanzahl()}")
    print(f"Anzahl Mitarbeiter: {firma.mitarbeiter_anzahl()}")
    print(f"Anzahl Abteilungsleiter: {firma.abteilungsleiter_anzahl()}")
    groesste = firma.abteilung_groesste_mitarbeiterzahl()
    print(f"Größte Abteilung: {groesste.name} mit {groesste.mitarbeiterzahl()} Mitarbeitern")
    print(f"Prozent Frauen/Männer: {firma.prozent_frauen_maenner()}")

if __name__ == "__main__":
    main()
