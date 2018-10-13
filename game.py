from player import Player
from hand import Hand
from random import randint
from deck import Deck

class Game:

    MAX_PLAYERS = 9
    MAX_HAND_SIZE = 2 
    BIG_BLIND = 2  # in dollars
    SMALL_BLIND = int(BIG_BLIND / 2)
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
        
        #load a deck
        self.deck = Deck()

        #shuffle the deck
        self.deck.shuffleDeck()
        
        # determine if this is the first hand; if it is load the players and their stack sizes
        # if state == None:
        #     for player in table:

    def getDealerName(self):
        for player in self.table:
            if player.getDealerStatus() == True:
             p = player
        return p.getName()

    def getTableStatistics(self):
        return (
                str(len(self.table))+' players at the table.\n'
               #'Blinds are $'+ str(self.SMALL_BLIND) +'/$'+ str(self.BIG_BLIND)+'.'
               + self.getBlinds()
               +'\n' + self.getDealerName() + ' is the Dealer.'
        ) 

    def seatPlayers(self, table):
        self.table = table
        
    def getListofPlayers(self):
        return self.table

    #assumption with this method. Players must be loaded in first before calling this step
    def pickDealer(self):
        player = randint(0,len(self.table)-1) #pick a random player
        self.table[player].setDealerStatus(True) #set their Dealer status to true

    # def showDeck(self):
    #     self.deck.displayDeck()

    def dealNewHand(self,Player):
        cards_left = self.MAX_HAND_SIZE
        while(cards_left > 0):
            Player.hand.addCard(self.deck.deal())
            cards_left = cards_left - 1

    def getBlinds(self):
        return 'Blinds are $'+ str(self.SMALL_BLIND) +'/$'+ str(self.BIG_BLIND)+'.'

    
 

        