class PokerUtil:

    def isPair(self,hand):
        '''
            @parameter Hand object
            @return boolean if hand is a pair or not
        '''
        for rank in hand.getHandRanks():
            if hand.getHandRanks().count(rank) > 1:
                return True
            else:
                return False
        
            
            