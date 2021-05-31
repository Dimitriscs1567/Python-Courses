import unittest
import sys
sys.path.append("milestone_2_course/models")

from card import Card

class CardTest(unittest.TestCase):

    def test_getValueFromName(self):
        card0 = Card("A*")
        card1 = Card("10*")
        card2 = Card("K*")
        card3 = Card("5*")

        self.assertEquals(card0.value, 1)
        self.assertEquals(card1.value, 10)
        self.assertEquals(card2.value, 10)
        self.assertEquals(card3.value, 5)


if __name__ == "__main__":
    unittest.main()