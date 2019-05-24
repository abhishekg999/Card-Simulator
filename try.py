from cardgames import *
import time
import sys

@functime
def main():
	deck = Deck()



	ctr = 0

	sf = s = f = t = p = 0

	log = False

	if len(sys.argv) != 1:
		tries = int(sys.argv[1])
	else:
		print("Default tries 100000")
		tries = 100000

	if tries > 1000000:
		print("Turining off log, too many tries... please wait")
		log = False

	if log:
		file = open("log.txt", "w+")
		print("Writing logfile..")
		
	time.sleep(.1)	
	try:
		for _ in range(tries):

			deck.collect()
			deck.shuffle()
			hand = deck.deal(3)
			ctr += 1 

			

			temp = str(pokerhands(hand))

			if log:
				file.write(str(hand))
				file.write(temp + "\n")

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

			print str(ctr)," Hands Played         \r",
		

	except KeyboardInterrupt:
		pass
	print("\n")

	print("Hangs Played: " + str(ctr))
	print("Straight Flush: " + str(sf) + ", " + str((float(sf)/float(ctr))*100.0) + "%")
	print("Three of a Kind: " + str(t) + ", " + str((float(t)/float(ctr))*100.0) + "%")
	print("Straight: " + str(s) + ", " + str((float(s)/float(ctr))*100.0) + "%")
	print("Flush: " + str(f) + ", " + str((float(f)/float(ctr))*100.0) + "%")
	print("Pair: " + str(p) + ", " + str((float(p)/float(ctr))*100.0) + "%")
	print("None: " + str(ctr - (s+f+sf+t+p)) + ", " + str((float(ctr - (s+f+sf+t+p))/float(ctr))*100.0) + "%")

main()




