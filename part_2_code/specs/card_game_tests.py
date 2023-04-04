import unittest
from src.card import *
from src.card_game import *

class TestCardGame(unittest.TestCase):
    def SetUp(self):
        self.card_1 = Card("diamonds", 7)
        self.card_2 = Card("hearts", 3)
        self.card_3 = Card("spades", 1)

        cards = [self.card_1, self.card_2, self.card_3]
        

    def test_check_for_an_ace(self):
        card_3 = Card("spades", 1)
        cardgame_1 = CardGame()
        result = cardgame_1.check_for_ace(card_3)
        self.assertEqual(True, result)
        

    def test_can_get_highest_card(self):
        card_1 = Card("diamonds", 7)
        card_2 = Card("hearts", 3)
        cardgame_1 = CardGame()
        result = cardgame_1.highest_card(card_1, card_2)
        self.assertEqual("diamonds", result.suit)


    def test_can_get_total(self):
        card_1 = Card("diamonds", 7)
        card_2 = Card("hearts", 3)
        card_3 = Card("spades", 1)
        cardgame_1 = CardGame()
        cards = [card_1, card_2, card_3]
        result = cardgame_1.cards_total(cards)
        self.assertEqual("You have a total of 11", result)