# imported to checked against the Broadway Straight (hardcoded for now)
# Example: A K Q J 10
import collections as collections 
class PokerUtil:

    def handPairRank(self,Hand):
        '''
            returns the sum of the count of rank in the Hand
        '''
        pairList = []
        hand_ranks = Hand.getHandRanks()

        for rank in hand_ranks:
            pairList.append(hand_ranks.count(rank))

        zip_pair_list = list(zip(pairList,hand_ranks))
        result = []

        for pairCount,rank in zip_pair_list:
            if pairCount >= 2:
                result.append((rank,pairCount))
        
        set_result = list(set(result))

        # can't distinguish between two pair and quads
        # run logic to determine which is the result and structure the result

        if len(result) == 4: 
            if len(set_result) == 2:
                return ('Two Pair',set_result,2)
            else:    
                return ('Four of a Kind',set_result, 7)
        else:
            pairDict = {
                2: ('Pair',set_result, 1), # (description of ranking, rank, strength)
                3: ('Three of a Kind',set_result, 3),
                5: ('Full House',set_result,6) # figure out how to get the correct list [trips rank,pair rank]
            }
            return pairDict[len(result)] 

    def isStraight(self,Hand):
        '''
            A method that will return if a Hand provided is a Straight
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
            Determine if a hand is Flush
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

        if flush:
            if straight:
                return ('Straight Flush', 8)
            else:
                return ('Flush', 5)
        elif straight:
            return ('Straight', 4)
        else:
            return ('Nothing', 0)

    def handRanking(self,Hand):
        '''
            determines the ranking of hands and returns a tuple containing the hand name and value 
        '''
        sumPair = self.handPairRank(Hand)
        
        if sumPair == Hand.getMaxSize():
          
            return self.flushOrStraight(Hand)
        else:
            pairDict = {
                #5: self.flushOrStraight,
                7:('Pair',1),
                9:('Two Pair',2),
                11:('Three of a Kind',3),
                13:('Full House',6),
                17:('Quads',7)
            }
            return pairDict[sumPair]
        
  


    
            
            