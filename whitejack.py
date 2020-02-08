####This is the blackjack problem procedural way of solving#######

import random
dealer_cards = []
player_cards = []

while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1,11))
    if len(dealer_cards) == 2:
        print("Dealer has x and {}".format(dealer_cards[1]))

while len(player_cards) != 2:
    player_cards.append(random.randint(1,11))
    if len(player_cards) == 2:
        print("you have {}".format(player_cards))

    if sum(dealer_cards) == 21:
        print("dealer has 21 and wins")
    elif sum(dealer_cards) > 21:
        print("dealer has last")

while sum(player_cards) < 21:
    action = str(input("Do you want to stay or hits?"))
    if action == "hit":
        player_cards.append(random.randint(1,11))
        print("you have total" + str(sum(player_cards)) + "from these cards",player_cards)
    if sum(dealer_cards) > sum(player_cards):
        print("dealer wins!")
    else:
        print("player wins")
        break



if sum(player_cards) > 21:
    print("you loose!")

elif sum(player_cards) > 21:
    print("you loose!")

elif sum(player_cards) == 21:
    print("you have blackjack")

