def list_comprehension(r):
    ungeradeZahlen = [zahl for zahl in range(r) if zahl % 2 == 1]
    return ungeradeZahlen

def set_comprehension(wort):
    vokale = {c  if c not in "aeiou" else "Vokal" for c in wort.lower()}
    return vokale

def dict_comprehension(woerter):

    laenge = {wort: len(wort) for wort in woerter}
    return laenge


def main():
    r = 10
    wort = "Ananassaft"
    woerter = ["Baumeister", "Christian", "Kiwi"]

    print(list_comprehension(r))
    print(set_comprehension(wort))
    print(dict_comprehension(woerter))

if __name__ == '__main__':
    main()
