####This is the blackjack problem procedural way of solving#######

import random
dealer_cards = []
player_cards = []

while len(dealer_cards) =! 2:
    dealer_cards.append(random.randint(1,11))
    if len(dealer_cards) == 2:
        print("Dealer has x and {}".format(dealer_cards[1]))