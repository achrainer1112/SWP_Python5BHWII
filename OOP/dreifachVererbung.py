class Lebewesen:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def essen(self):
        print(f"{self.name} isst.")

    def schlafen(self):
        print(f"{self.name} schläft.")


class Mensch(Lebewesen):
    def __init__(self, name, alter, geschlecht):
        super().__init__(name, alter)
        self.geschlecht = geschlecht

    def sprechen(self, text):
        print(f"{self.name} sagt: {text}")



class Schueler(Mensch):
    def __init__(self, name, alter, geschlecht, klasse):
        super().__init__(name, alter, geschlecht)
        self.klasse = klasse

    def lernen(self):
        print(f"{self.name} lernt.")


def main():
    schueler = Schueler("Andreas", 19, "male", "5BHWII")
    schueler.essen()
    schueler.schlafen()
    schueler.sprechen("Hallo!")
    schueler.lernen()

if __name__ == "__main__":
    main()

