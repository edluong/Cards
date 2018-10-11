from player import Player
from hand import Hand

class Game:
    MAX_PLAYERS = 9
    MAX_HAND_SIZE = 2 
    BIG_BLIND = 2  # in dollars
    SMALL_BLIND = BIG_BLIND / 2
    MAX_BUYIN = BIG_BLIND * 100


    '''
        Holds a game of Texas Hold'em Poker

        requirements:
        - defines max players
        - defines max hand size
        - defines the blind size

        - provide number of players at table
        - determine which game state (starting,preflop,postflop,turn,river,showdown)
        - provide the pot size
        - deals the cards
        - check for winner (determines the best hand)
    '''
    def __init__(self, table = None, potSize = 0, state = None):
        if table == None:
            self.table = [] # players at this table
        else:
            self.table = table
        self.board = [] # showing the cards that are dealt
        self.pot = potSize # keep track of the pot
        
        # determine if this is the first hand; if it is load the players and their stack sizes
        # if state == None:
        #     for player in table:
                


    def getTableStatistics(self):
        return (
                str(len(self.table))+' players at the table.\n'
               'Blinds are $'+ self.SMALL_BLIND +'/$ '+ self.BIG_BLIND
        ) 

    def seatPlayers(self, table):
        self.table = table
        
    def getListofPlayers(self):
        return self.table

    #assumption with this method. Players must be loaded
    def pickDealer(self):
        pass