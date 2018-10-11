from hand import Hand

class Player:
    '''
        Player of a Texas Holdem Game

        Requirements:
        - Is the dealer or not
        - Has chips (stack size)
        - Can bet (call, raise, fold) (decrease the stack size)
        - Has a name
        - can display hand
    '''

    def __init__(self,name,isDealer = False,stackSize = 0,hand = None):
        if hand == None:
            hand = Hand([])
        self.name = name
        self.hand = hand
        self.cards = hand.hand
        self.isDealer = isDealer
       
    def getStackSize(self):
        return self.stackSize
    
    def setStackSize(self,stackSize):
        self.stackSize = stackSize

    def bet(self,betAmount):
        newStackSize = self.stackSize - betAmount
        if newStackSize < 0:
            print('!!!')
            print(' Stack size is: '+ str(self.stackSize) +' and bet amount is: '+ str(betAmount))
            print(" Can't bet more than your stack!")
            print('!!!')
        else:
            self.stackSize = self.stackSize - betAmount
   
    def getHeldHand(self):
        return self.cards  
    
    def setDealerStatus(self,status):
        self.isDealer = status
    
    def getDealerStatus(self):
        return self.isDealer


        
        
