from cardgames import *
import time
import sys
import threading

mdict = {'sf':0, 's':0, 'f':0, 't':0, 'p':0, 'tries':0}
def handler(tries):
	deck = Deck()

	ctr = 0

	sf = s = f = t = p = 0
	
	try:
		for _ in range(tries):

			deck.collect()
			deck.shuffle()
			hand = deck.deal(3)
			ctr += 1 
			temp = str(pokerhands(hand))


			if temp == "Straight Flush":
				sf += 1


			elif temp == "Straight":
				s += 1

			elif temp == "Flush":
				f += 1

			elif temp == "Three of a Kind":
				t += 1

			elif temp == "Pair":
				p += 1

	except KeyboardInterrupt:
		pass
	mdict['sf'] += sf
	mdict['s'] += s
	mdict['f'] += f
	mdict['t'] += t
	mdict['p'] += p
	mdict['tries'] += ctr



@functime
def main():
	threads = []
	for a in range(100):
		t = threading.Thread(target=handler, args=[1000])
		t.setDaemon(True)
		threads.append(t)

	for a in threads:
		a.start()

	for a in threads:
		a.join()

	ctr = mdict['tries']
	sf = mdict['sf']
	t = mdict['t']
	s = mdict['s']
	p = mdict['p']
	f = mdict['f']
	print("Hangs Played: " + str(ctr))
	print("Straight Flush: " + str(sf) + ", " + str((float(sf)/float(ctr))*100.0) + "%")
	print("Three of a Kind: " + str(t) + ", " + str((float(t)/float(ctr))*100.0) + "%")
	print("Straight: " + str(s) + ", " + str((float(s)/float(ctr))*100.0) + "%")
	print("Flush: " + str(f) + ", " + str((float(f)/float(ctr))*100.0) + "%")
	print("Pair: " + str(p) + ", " + str((float(p)/float(ctr))*100.0) + "%")
	print("None: " + str(ctr - (s+f+sf+t+p)) + ", " + str((float(ctr - (s+f+sf+t+p))/float(ctr))*100.0) + "%")

main()







