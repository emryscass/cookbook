import random

class Card:
    # Pass the number as a string to pair with JQKA
    def __init__(self, suit, number):
        self._suit = suit
        self.number = number

    # Redefine __repr__ to represent the cards in a meaningful manner
    def __repr__(self):
        return self.number + " of " + self.suit


    # Return the value of the _suit attribute
    # Add a decorator to say that it is a property
    @property
    def suit(self):
        return self._suit


    @suit.setter
    def suit(self, suit):
        if suit in ['hearts', 'clubs', 'diamonds', 'spades']:
            self._suit = suit
        else:
            print('That\'s not a suit!')



class Deck:
    def __init__(self):
        self._cards = []
        self.populate()
        print(self._cards)



    def populate(self):
        suits = ['hearts', 'clubs', 'diamonds', 'spades']
        numbers = [
        '2', '3', '4', '5', '6',
        '7', '8', '9', '10',
        'J', 'Q', 'K', 'A'
        ]

        cards = []
        self._cards = [Card(s, n) for s in suits for n in numbers]
        shuffled = random.shuffle(self._cards)
        return shuffled




my_deck = Deck()
