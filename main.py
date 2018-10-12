from game import Game
from player import Player
from hand import Hand

'''
    Interface with the player
    - Takes input
    - determine winner
    - pay out pot
    - deals new hand
'''
#create the game and the table to seat the Players
g = Game()
table = []
gameloop = True

#load the players
#-- load the "hero" or person playing against CPU
playerName = input('Enter name: ')
buyIn = input('How much to buy in (MAX Buy In is: '+ str(g.MAX_BUYIN) +'): ')
hero = Player(playerName,stackSize = buyIn,hand = Hand(g.MAX_HAND_SIZE))

#print('hero stack size: '+ str(hero.getStackSize()))

#-- load hardcoded CPU
robot = Player('CPU1',stackSize = g.MAX_BUYIN,hand = Hand(g.MAX_HAND_SIZE))
#print('robot stack size: '+ str(robot.getStackSize()))

#-- seat the players so the game can pick who is dealer
#--- seat the players at the table
table.append(hero)
table.append(robot)
#---associate the table to the game
g.seatPlayers(table)

#pick the dealer and then print out the table statistics
g.pickDealer()
print(g.getTableStatistics())

g.dealNewHand(hero)
for card in hero.getHeldHand():
    print(card)

g.dealNewHand(robot)
for card in robot.getHeldHand():
    print(card)















