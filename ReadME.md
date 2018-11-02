TO DO:
- rewrite getPairList() -> PairCountSort(self,Hand):
- requirements: returns a Hand now. sorts the hand based on pair count and strength of card


- make the methods in PokerUtil static
- write a compareHands pokerUtil function to determine the winning hand; need to modify the tuple that handRanking returns

Bug fixes:
- add a try catch to buy in clause in main.py 

Low:
- write a robot class that extends a player. So the robot can use the starting hand strength function
- write a function to rank starting hand strength (useful for new players)