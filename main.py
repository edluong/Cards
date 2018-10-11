from game import Game
from player import Player

#create the game and the table to seat the Players
g = Game()
table = []
gameloop = True

#load the players
#-- load the "hero" or person playing against CPU
playerName = input('Enter name: ')
buyIn = input('How much to buy in (MAX Buy In is:'+ str(g.MAX_BUYIN) +'): ')
hero = Player(playerName,stackSize = buyIn)

print('hero stack size: '+ str(hero.getStackSize()))

#-- load hardcoded CPU
robot = Player('CPU1',stackSize = g.MAX_BUYIN)
print('robot stack size: '+ str(robot.getStackSize()))

#-- seat the players so the game can pick who is dealer
#--- seat the players at the table
table.append(hero)
table.append(robot)
#---associate the table to the game
g.seatPlayers(table)
print(g.getListofPlayers())















