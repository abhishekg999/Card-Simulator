import time
from cardgames import *
import threading

mdict = {'sf':0, 's':0, 'f':0, 't':0, 'p':0, 'tries':0}

def func():
	"""
	deck = cardgames.Deck()
	time.sleep(.5)

	for _ in range(100):
		time.sleep(.01)
	"""

	tries = 1000

	deck = Deck()

	ctr = 0

	sf = s = f = t = p = 0
	
	for _ in range(tries):

		deck.collect()
		deck.shuffle()
		hand = deck.deal(3)
		ctr += 1 
		temp = str(pokerhands(hand))


		if temp == "Straight Flush":
			mdict['sf'] += 1


		elif temp == "Straight":
			mdict['s'] += 1

		elif temp == "Flush":
			mdict['f'] += 1

		elif temp == "Three of a Kind":
			mdict['t'] += 1

		elif temp == "Pair":
			mdict['p'] += 1

	mdict['tries'] += ctr


@functime
def main():
	threads = []

	for x in range(10):
		t = threading.Thread(target=func)
		t.setDaemon(True)
		threads.append(t)

	for x in threads:
		x.start()

	for x in threads:
		x.join()

	print mdict

main()


