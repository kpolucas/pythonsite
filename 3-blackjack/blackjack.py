import random
import os

def handValue(cards):
    total = 0
    aces = []
    for card in cards:
        if card in ['J','Q','K']:
            total += 10
        elif card in [2,3,4,5,6,7,8,9]:
            total += card
        else:
            aces.append(card)
    for ace in aces:
        if total <= 10:
            total += 11
        else:
            total += 1
    return total

def whoWins(you,them):
    pass

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

while True:
    os.system('clear')
    print('Your hand   [{}] {}'.format(']['.join(str(p) for p in playerHand),handValue(playerHand)))
    print('Casino hand [{}][{}]'.format(casinoHand[0],'?'))
    print('another card?')
    anotherCard = input()
    if anotherCard == 'y':
        playerHand.append(deck.pop(0))
    if anotherCard == 'n':
        break
while handValue(casinoHand) <= 16:
    casinoHand.append(deck.pop(0))

os.system('clear')
print('Your hand   [{}] {}'.format(']['.join(str(p) for p in playerHand),handValue(playerHand)))
print('Casino hand [{}] {}'.format(']['.join(str(p) for p in casinoHand),handValue(casinoHand)))

#Codear whoWins
#whoWins(handValue(yourHand),handValue(casinoHand))
