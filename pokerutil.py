class PokerUtil:

    def isPair(self,Hand):
        '''
            @parameter Hand object
            @return boolean if hand is a pair or not
        '''
        for rank in Hand.getHandRanks():
            if Hand.getHandRanks().count(rank) > 1:
                return True
            else:
                return False
    
    def handPairSum(self,Hand):
        '''
            returns the sum of the count of rank in the Hand
        '''
        pairList = []
        for rank in Hand.getHandRanks():
            pairList.append(Hand.getHandRanks().count(rank))
        return sum(pairList)

    def flushOrStraight(self,Hand):
        return ('flush or straight',4)

    def handRanking(self,Hand):
        '''
            determines the ranking of hands and returns a tuple containing the hand name and value 
        '''
        sumPair = self.handPairSum(Hand)

        if sumPair == 5:
            return self.flushOrStraight(Hand)
        else:
            pairDict = {
                5: self.flushOrStraight,
                7:('pair',1),
                9:('two pair',2),
                11:('Three of a kind',3),
                13:('Full House',6),
                17:('Quads',7)
            }
            return pairDict[sumPair]
        
  


    
            
            