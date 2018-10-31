class Hand:
    '''
        representing a hand in card games

        requirements:
        - provide the exact cards in hand
        - provide the number of cards
        - score the hand; using the cards with the board
    '''

    def __init__(self,maxSize):
        self.hand = []
        self.maxSize = maxSize

    def getHandSize(self):
        return len(self.hand)
    
    def getHeldCards(self):
        return self.hand
    
    def getMaxSize(self):
        return self.maxSize
    
    def addCard(self,Card):
        self.hand.append(Card)

    def getHandRanks(self):
        rank = []
        for card in self.hand:
            rank.append(card.getRank()) 
        return rank