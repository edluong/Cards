class Card:
    '''
        Implementation of a playing card.
    '''

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def displaySuit(self):
        print(self.suit)

    def displayRank(self):
        print(self.rank)

    '''
        toString function
        Prints out a human friendly message of what the card.
        example: King of Hearts if the input was Card('Heart',13)
    '''
    def __str__(self):
        #checks to see if the cards are within the "special" picture cards such as Ace,Jacks, etc...
        if self.rank in [1,11,12,13]:
            rankName = {
                1: 'Ace',
                11: 'Jack',
                12: 'Queen',
                13: 'King'
            }
            return rankName.get(self.rank,'Invalid Rank') + ' of ' + self.suit + 's'
        elif self.rank > 1 and self.rank <= 10:
            return str(self.rank) + ' of ' + self.suit + 's'
        else:
            return 'Invalid Card'