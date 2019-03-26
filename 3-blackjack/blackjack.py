import random

def handValue(cards):
    # Falta evaluar el caso de A = 1 o A = 11
    total = 0
    for card in cards:
        if card in ['J','Q','K','A']:
            total += 10
        else:
            total += card
    return total

deck = [
2,3,4,5,6,7,8,9,'J','Q','K','A',
2,3,4,5,6,7,8,9,'J','Q','K','A',
2,3,4,5,6,7,8,9,'J','Q','K','A',
2,3,4,5,6,7,8,9,'J','Q','K','A',
]

playerHand = []
casinoHand = []

random.shuffle(deck)
playerHand.append(deck.pop(0))
playerHand.append(deck.pop(0))

casinoHand.append(deck.pop(0))
casinoHand.append(deck.pop(0))

print(playerHand)
print(casinoHand)

print(handValue(playerHand))
print(handValue(casinoHand))
