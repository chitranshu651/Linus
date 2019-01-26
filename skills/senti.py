#
#	Enter sentence in command line argument
#	it will return whether person is consistent sad or not
#	return 1 = sad
#	return 0 = not sad
#


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sys

analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
	score = analyser.polarity_scores(sentence)
	fNeg = open(".neg.txt","a+")
	fNeu = open(".neu.txt","a+")
	fPos = open(".pos.txt","a+")
	fCompaund = open(".com.txt","a+")
	fNeg.write(str(score['neg'])+"\n")
	fNeu.write(str(score['neu'])+"\n")
	fPos.write(str(score['pos'])+"\n")
	fCompaund.write(str(score['compound'])+"\n")
	fNeg.close()
	fNeu.close()
	fPos.close()
	fCompaund.close()

def isSad():
	lines = [line.rstrip('\n') for line in open('.neg.txt')]
	sum=0
	ln=len(lines)
	if ln > 15:
		ln = 15

	for i in range(ln):
		sum+=float(lines[i])
	if (sum/ln > 0.5):
		return 1
	else:
		return 0



sentiment_analyzer_scores(sys.argv[1])
print (isSad())
