from Card import Card
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Deck:
    '''
    Class for a deck made up of multiple decks of Cards.
    '''
    def __init__(self, deck_number=1):
        self.all_cards = []
        for x in range(deck_number):
            for suit in suits:
                for rank in ranks:
                    # create the individual card and add them to the deck
                    self.all_cards.append(Card(suit, rank))

    def __len__(self):
        return len(self.all_cards)

    def shuffle(self):
        '''
        Function to shuffle the cards in the deck
        '''
        random.shuffle(self.all_cards)

    def deal_one(self):
        '''
        Function to deal one card from the deck
        '''
        return self.all_cards.pop()

    def deal_between(self, *args):
        '''
        Function to deal the deck between any number of players
        '''
        while len(self.all_cards) > 0:
            for player in args:
                player.hand.append(self.deal_one())
