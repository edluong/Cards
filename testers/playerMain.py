from player import Player

ed = Player('Ed')

ed.setStackSize(100)
print(ed.name +' bought in for '+ str(ed.getStackSize()))

#test betting
ed.bet(20)
print(ed.name +"'s Stack size is: "+ str(ed.getStackSize()))
ed.bet(200)

print(ed.getHeldHand())

print(ed.getDealerStatus())
ed.setDealerStatus(True)
print(ed.getDealerStatus())