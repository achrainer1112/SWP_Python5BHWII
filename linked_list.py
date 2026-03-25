import random


class ListElement:
    def __init__(self, obj):
        self.obj = obj
        self.nextElem = None


class LinkedList:

    def __init__(self):
        self.start = ListElement("Kopf")
        self.size = 0

    def addLast(self, obj):
        new = ListElement(obj)
        last = self.getLast()
        last.nextElem = new
        self.size += 1

    def getLast(self):
        pointerElem = self.start
        while pointerElem.nextElem:
            pointerElem = pointerElem.nextElem
        return pointerElem

    def length(self):
        return self.size

    def writeList(self):
        pointerElem = self.start
        while pointerElem:
            print(pointerElem.obj)
            pointerElem = pointerElem.nextElem

    def __iter__(self):
        pointerElem = self.start.nextElem
        while pointerElem:
            yield pointerElem.obj
            pointerElem = pointerElem.nextElem


def main():
    list = LinkedList()

    values = random.sample(range(1, 101), 8)

    for v in values:
        list.addLast(v)

    print("Länge:", list.length())
    list.writeList()

    print("Summe:", sum(list))
    print("Max:", max(list))
    print("Min:", min(list))


if __name__ == "__main__":
    main()