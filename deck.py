#performing list operations in functions
# let's play a game of hearts :-)

def newDeck():
    suits = ("Hearts", "Spades", "Diamonds", "Clubs")
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    deck = []

    for  suit in suits:
        for rank in ranks:
            deck.append(f'{ranks} of {suits}')

    return deck

newDeck()