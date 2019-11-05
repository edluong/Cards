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

    def __init__(self,name,isDealer = False,turnState = None,stackSize = 0,hand = None):
        self.turnState = turnState
        self.stackSize = stackSize
       
    def getStackSize(self):
        return self.stackSize
    
    #set the stack size of the Player
    def setStackSize(self,stackSize):
        self.stackSize = stackSize
    
    #get the name of the Player
    def getName(self):
        return self.name

    def bet(self,betAmount):
        newStackSize = self.stackSize - betAmount
        if newStackSize < 0:
            errorMsg = '''
    !!!
    Stack size is: {} and bet amount is {}
    Can't bet more than your stack!
    !!!
            '''
            print(errorMsg.format(str(self.stackSize),str(betAmount)))

        else:
            self.stackSize = self.stackSize - betAmount
   
    def getHeldHand(self):
        heldhand = self.name + ': '
        for card in self.hand.getHeldCards():
            heldhand += '(' + str(card)+ ')' +' '  
        return heldhand
    
    def setDealerStatus(self,status):
        self.isDealer = status
    
    def getDealerStatus(self):
        return self.isDealer


        
        
