class Player:
    '''
    Class for an individual player in the blackjack game
    '''

    def __init__(self, name, chips):
        self.name = name
        self.hand = []
        self.chips = chips
        self.current_bet = 0

    def __str__(self):
        return f'Player {self.name} has {self.chips} chips'

    def display_hand(self):
        '''
        Function to display the hand. Prints each card on a new line.
        '''
        print(f"{self.name}'s current hand is: ")
        for card in self.hand:
            print(card)

    def hand_value(self):
        '''
        Function to calculate the value of a hand, reduces aces to 1
        if the player would go bust.
        '''
        hand_sum = 0
        ace_count = 0
        for card in self.hand:
            hand_sum += card.value
            if card.value == 11:
                ace_count += 1
        # account for aces being 1 or 11
        while hand_sum > 21 and ace_count > 0:
            hand_sum -= 10
            ace_count -= 1
        return hand_sum

    def bet_amount(self):
        '''
        Function to ask how much a player would like to bet and remove the bet
        from the players chips.
        '''
        bet = 0
        while True:
            try:
                bet = int(input(f'How much would {self.name} like to bet? '))
            except ValueError:
                print("That is not a suitable number of chips, try again.")
                continue
            if bet > self.chips:
                print("You don't have enough chips, choose a lower amount.")
                continue
            break
        self.chips -= bet
        self.current_bet = bet

    def modify_hand(self, deck):
        '''
        Function to ask if the player wants to hit or stand displaying the hand
        after each hit. Continues until the player stands or goes bust.
        '''
        while True:
            if self.is_bust():
                print("You have gone bust!")
                break
            hit_action = " "
            while hit_action not in ["Y", "N"]:
                hit_action = input(f"Player {self.name} would you like to hit? (Y/N)").upper()
                if hit_action not in ["Y", "N"]:
                    print("Please input 'Y' or 'N'.")
            if hit_action == "Y":
                self.hand.append(deck.deal_one())
                self.display_hand()
            else:
                print(f"Player {self.name} has stood.")
                break

    def is_bust(self):
        '''
        Function to calculate if the players hand is over 21.
        '''
        # can condense
        hand_value = self.hand_value()
        if hand_value > 21:
            return True
        else:
            return False

    def initial_deal(self, deck):
        '''
        Function to deal the initial two cards and display them.
        '''
        self.hand.append(deck.deal_one())
        self.hand.append(deck.deal_one())
        self.display_hand()

    def payout(self):
        '''
        Function to return double the bet to the player and clear
        the current_bet attribute.
        '''
        self.chips += (self.current_bet*2)
        print(f"Player {self.name} won {self.current_bet*2} chips.")
        self.current_bet = 0

    def draw_payout(self):
        '''
        Funtion to return the bet chips to the player in case of a draw and
        clear the current_bet attribute.
        '''
        self.chips += self.current_bet
        print(f"Player {self.name} draw {self.current_bet} chips have been returned.")
        self.current_bet = 0
