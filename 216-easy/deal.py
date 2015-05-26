from random import shuffle

# Program input
nbPlayers = int(input())

# Global vars setup
deck = [x for x in range(52)]
shuffle(deck)
players = []
table = []

# Helper functions

def deal(n):
	return [deck.pop(1) for x in range(n)]
	
def printCard(n):
	s = n % 4
	v = n % 13
	suit = "hearts" if s == 0 else "diamonds" if s ==1 else "spades" if s == 2 else "clubs"
	value = "ace" if v == 0 else "jack" if v == 10 else "queen" if v == 11 else "king" if v == 12 else str(v+1)
	print("\t{} of {}".format( value, suit))
	
def printTable():
	for i in range(nbPlayers):
		print("Player ", i+1)
		for n in range(len(players[i])):
			printCard(players[i][n])
			
	print("Community cards")
	for i in range(len(table)):
		printCard(table[i])

# Main program

# Deal to all players
for i in range(nbPlayers):
	players.append(deal(2))

# Deal community cards
table = deal(5)

printTable()
