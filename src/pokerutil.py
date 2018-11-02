# imported to checked against the Broadway Straight (hardcoded for now)
# Example: A K Q J 10
import collections as collections 
class PokerUtil:

    def getPairList(self, Hand, pairDef = 2):
        # is it bad practice to just have a parameter to define what
        # a pair is here?
        # Thought process is that needed same method for every card
        # So no need to rewrite if I have a parameter
        '''
        Returns a list that has the Rank and "Pairness" count associated
        with the card.

        pairDef = the number that is defined to be a "pair". Default to 2
        if getPairList(Hand,1) is used then it will return every card 
        '''
        pairList = []
        hand_ranks = Hand.getHandRanks()

        for rank in hand_ranks:
            pairList.append(hand_ranks.count(rank))

        zip_pair_list = list(zip(pairList,hand_ranks))
        result = []

        for pairCount,rank in zip_pair_list:
            if pairCount >= pairDef:
                result.append((rank,pairCount))
        
        return result


    def handPairRank(self,Hand):
        '''
            classification method:
            @return: result tuple
        '''
        result = self.getPairList(Hand)
        set_result = list(set(result))

        # can't distinguish between two pair and quads
        # run logic to determine which is the result and structure the result
        if len(result) == 4: 
            if len(set_result) == 2:
                return (2,'Two Pair',set_result)
            else:    
                return (7,'Four of a Kind',set_result)
        else:
            pairDict = {
                0: (0,'Nothing',[Hand.getMaxRank()]),
                2: (1,'Pair',set_result), # (description of ranking, rank, strength)
                3: (3,'Three of a Kind',set_result),
                5: (6,'Full House',set_result) # figure out how to get the correct list [trips rank,pair rank]
            }
            return pairDict[len(result)] 

    def isStraight(self,Hand):
        '''
            classification method
            A method that will return if a Hand provided is a Straight
            @return boolean
        '''

        #initialize method variables
        count = 0 
        BROADWAY = [1,10,11,12,13] # biggest possible straight in poker; nickname for it
        hand_rank = []
        for card in Hand.getHeldCards():
            hand_rank.append(card.getRank())
        hand_size = Hand.getHandSize()
        hand_rank.sort()
        
        # compare if the next element in the list of ranks to see if it is 1 larger
        for i in range(0,hand_size-1):
            if hand_rank[i + 1] == hand_rank[i] + 1:
                count += 1

        # count how many card rank are 1 greater than the previous suit 
        # OR check if the straight is a Broadway straight 
        if count == hand_size - 1 or collections.Counter(hand_rank) == collections.Counter(BROADWAY):
            return True
        else:
            return False 

    def isFlush(self,Hand):
        '''
            Classification method
            Method to determine if there is a flush from a Hand
            @return boolean
        '''
        #initiate some method variables
        hand = Hand.getHeldCards()
        hand_suit = []

        for card in hand:
            hand_suit.append(card.getSuit())

        # if there is only one type of suit in the hand
        # forcing the list into a set will delete the duplicates therefore the set should only be left with 1 suit
        if len(set(hand_suit)) == 1: 
            return True
        else:
            return False

    def flushOrStraight(self,Hand):
        
        #check for flush, if true double check for straight
        flush = self.isFlush(Hand)
        straight = self.isStraight(Hand)

        minCardRank = Hand.getMinRank()
        maxCardRank = Hand.getMaxRank()

        result = [minCardRank,maxCardRank]

        if flush:
            if straight:
                return (8,'Straight Flush',result)
            else:
                return (5,'Flush', result)
        elif straight:
            return (4,'Straight', result)
        else:
            return (0,'Nothing', [Hand.getMaxRank()])

    def handRanking(self,Hand):
        # adds the result of a pair hand evaluation and a flush or straight evaluation
        # chooses to return the higher of the two evaluations 
       return max([self.handPairRank(Hand),self.flushOrStraight(Hand)],key=lambda x:x[0])            