def combine_tweets(tweets):
	words = []
	for t in tweets:
		words += t.split()
	return words