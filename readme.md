TO DO:
- rewrite handRanking method due to new HandPairRank (take in account of 7 cards)
- make the methods in PokerUtil static
- write a compareHands pokerUtil function to determine the winning hand; need to modify the tuple that handRanking returns

Bug fixes:
- add a try catch to buy in clause in main.py 

Low:
- write a robot class that extends a player. So the robot can use the starting hand strength function
- write a function to rank starting hand strength (useful for new players)