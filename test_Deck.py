import unittest
from Deck import Deck
from Player import Player


class TestDeck(unittest.TestCase):

    def test_shuffle(self):
        deck = Deck()
        deck2 = deck
        deck.shuffle()
        self.assertCountEqual(deck.all_cards, deck2.all_cards,
                              'Cards go missing')
        self.assertEqual(len(
            set(deck.all_cards).intersection(set(deck2.all_cards))), 52)

    def test_deal_one(self):
        deck = Deck()
        deck.deal_one()
        self.assertEqual(len(deck.all_cards), 51)

    def test_deal_between_two(self):
        deck = Deck()
        player1 = Player('name', 10)
        player2 = Player('name', 10)
        deck.deal_between(player1, player2)
        self.assertEqual(len(player1.hand), 26, '26 cards not in player1 hand')
        self.assertEqual(len(player2.hand), 26, '26 cards not in player2 hand')
        self.assertEqual(len(deck.all_cards), 0, 'cards left in deck')

    def test_deal_between_four(self):
        deck = Deck()
        player1 = Player('name', 10)
        player2 = Player('name', 10)
        player3 = Player('name', 10)
        player4 = Player('name', 10)
        deck.deal_between(player1, player2, player3, player4)
        self.assertEqual(len(player1.hand), 13, '13 cards not in player1 hand')
        self.assertEqual(len(player2.hand), 13, '13 cards not in player2 hand')
        self.assertEqual(len(player3.hand), 13, '13 cards not in player3 hand')
        self.assertEqual(len(player4.hand), 13, '13 cards not in player4 hand')
        self.assertEqual(len(deck.all_cards), 0, 'cards left in deck')


if __name__ == '__main__':
    unittest.main()
