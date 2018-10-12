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
    
    def addCard(self,Card):
        self.hand.append(Card)
    
    def isWinningHand(self):
        pass # implement later