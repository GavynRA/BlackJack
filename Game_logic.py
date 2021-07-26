from Player import Player
from Deck import Deck
from Dealer import Dealer


'''
Game logic:
Find new players that are playing
ask how much they want to bet
inital deal.
go player by player modifying hand
modify the dealers hand
use payout function to check who has won
ask if anyone wants to leave the table
'''

table_active = True
dealer = Dealer()
seated_players = []
while table_active:
    # loop to keep asking for players until a no is given.
    while True:
        player_join = input("Would anyone like to join? (Y/N)").upper()
        if player_join not in ["Y", "N"]:
            print("Please input 'Y' or 'N'.")
            continue
        elif player_join == "Y":
            # add a player with a name and chip amount to the seated players
            player_name = input("What is your name?").lower().capitalize()
            while True:
                try:
                    player_chips = int(input("How many chips would you like to buy in with?"))
                except ValueError:
                    print("That is not a suitable number of chips, try again.")
                    continue
                break
            seated_players.append(Player(player_name, player_chips))
            continue
        else:
            break
    # at the start of the round create a fresh deck if no deck exists
    try:
        deck
    except NameError:
        deck = Deck(3)
        deck.shuffle()
    # clear everyone's hand
    for player in seated_players:
        player.hand.clear()
    dealer.hand.clear()
    # ask each player how much to bet
    for player in seated_players:
        player.bet_amount()
    # deal each players cards then the dealers
    for player in seated_players:
        player.initial_deal(deck)
    dealer.initial_deal(deck)
    # ask players to hit or stick then have the dealer do it.
    for player in seated_players:
        player.modify_hand(deck)
    dealer.modify_hand(deck)
    # payout any winnings
    dealer.payout(seated_players)
    # delete the deck to save memory if there are too few cards left
    if len(deck) < 52:
        del deck
    # see if anyone wants to leave the table
    while True:
        # check if the table is empty then close the table if so
        if len(seated_players) == 0:
            table_active = False
            break
        player_leave = input("Would anyone like to leave the table? (Y/N)").upper()
        if player_leave not in ["Y", "N"]:
            print("Please input 'Y' or 'N'.")
            continue
        elif player_leave == "Y":
            player_num = len(seated_players)
            player_leave_name = input("What is the name of the leaving player?").lower().capitalize()
            for i, player in enumerate(seated_players):
                if player.name == player_leave_name:
                    print(f"{player} and has left the table")
                    del seated_players[i]
                    break
            if len(seated_players) == player_num:
                print(f"Player {player_leave_name} is not at the table")
            continue
        else:
            break
print("Thanks for playing, the table is closed.")
