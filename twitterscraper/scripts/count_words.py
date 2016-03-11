from collections import OrderedDict
def count_words(tweets):
	tweets = tweets.split()
	wordcount = dict()
	for w in tweets:
		if w in wordcount.keys():
			wordcount[w] = wordcount[w]+1
		else:
			wordcount[w] = 1
	ordered = OrderedDict(sorted(wordcount.items(), key = lambda kv: kv[1], reverse=True))
	return ordered