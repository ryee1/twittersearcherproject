def count_words(tweets):
	wordcount = dict()
	for w in tweets:
		if w in wordcount.keys():
			wordcount[w] = wordcount[w]+1
		else:
			wordcount[w] = 1
	return wordcount