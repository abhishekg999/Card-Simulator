import random
import time

def functime(func):
	def mep():
		start = time.time()
		func()
		print str(time.time() - start) + " seconds"

	return mep


class Deck():
	def __init__(self):
		self.deck = [n + " " + x for x in ["Spades", "Diamonds", "Hearts", "Clovers"] for n in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]
		self.table = []
		self.hands = []

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self, mt=1):
		self.t = []

	###### SHOULD WORK NOW ######
		try:
			for x in range(mt):
				self.t.append(self.deck[0])
				self.table.append(self.deck[0])
				del self.deck[0]
			#self.deck = list(set(self.deck) - set(self.t))
			#self.table = list(set(self.table) | set(self.t))
		except:
			print("Dealt " + str(len(self.t)) + " cards")
			print("Deck empty")
		return self.t
	


	def collect(self, collectall=True, *args):
		if collectall:
			for x in self.table:
				self.deck.append(x)

			self.table = []
			self.hands = []


#so far only works for 3 card hands
def pokerhands(cards, suit = ["Spades", "Diamonds", "Hearts", "Clovers"], number = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"], cardno = 3):
	numcnt = {}
	for n in number:
		numcnt[n] = 0
	suitcnt = {}
	for s in suit:
		suitcnt[s] = 0

	
	for s in suit:
		for c in cards:
			if s in c:
				suitcnt[s] += 1


	for x in cards:
		numcnt[x.split(" ")[0]] += 1

	flush = False
	for x in suitcnt:
		if suitcnt[x] == cardno:
			flush = True


	straight = False
	sctr = 0

	#print numcnt
	for x in number:

		if numcnt[x] == 1:
			sctr += 1
			if sctr == cardno:
				straight = True
		else:
			sctr = 0

		if x == "Q":
			if numcnt["Q"] == numcnt["K"] == numcnt["A"] == 1:
				straight = True

	toak = False
	if cards[0].split(" ")[0] == cards[1].split(" ")[0] == cards[2].split(" ")[0]:
		toak = True

	pair = False
	if (cards[0].split(" ")[0] == cards[1].split(" ")[0]) or (cards[1].split(" ")[0] == cards[2].split(" ")[0]) or (cards[0].split(" ")[0] == cards[2].split(" ")[0]):
		pair = True

	if flush and straight: 
		return ("Straight Flush")

	if toak:
		return ("Three of a Kind")

	if straight: 
		return ("Straight")

	if flush: 
		return ("Flush")

	if pair:
		return ("Pair")


	
	



		
