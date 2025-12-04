from Poker import hatPaar, hatDrilling, hatStrasse, hatRoyalFlush
import unittest

class TestPokerKombinationen(unittest.TestCase):

    def test_hatPaar(self):
        # Beispiel: Paar Könige
        karten = [(0, 13), (1, 13), (2, 5), (3, 7), (0, 9)]
        self.assertTrue(hatPaar(karten))

    def test_hatDrilling(self):
        # Beispiel: Drilling Damen
        karten = [(0, 12), (1, 12), (2, 12), (3, 4), (1, 9)]
        self.assertTrue(hatDrilling(karten))

    def test_hatStrasse(self):
        # Beispiel: Straße 5-6-7-8-9
        karten = [(0, 5), (2, 6), (1, 7), (3, 8), (2, 9)]
        self.assertTrue(hatStrasse(karten))

    def test_hatRoyalFlush(self):
        # Beispiel: Royal Flush in Herz
        karten = [(0, 10), (0, 11), (0, 12), (0, 13), (0, 14)]
        self.assertTrue(hatRoyalFlush(karten))

if __name__ == "__main__":
    unittest.main()
