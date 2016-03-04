from twython import Twython

APP_KEY = 'f1HlAsbabsoi3cr5EC3t1NzDH'
APP_SECRET = 'XSsoDYC4W1g2l3VUyU1vtTQ7SroB0olzDokpwD5CpgcRjMh715'
OAUTH_TOKEN = '	4760974394-ThpCcbIXGznm51P9RO2jjSsDdjWs8PHYkALk1KD'
OAUTH_TOKEN_SECRET = 'DFkoR2HMhImpfhoTNc3T7WNItqpxfxaE0ciwrFJj500Sd'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def hashtagfinder(word):
	results = twitter.search(q=word, count='100', lang='en')
	tweets = []
	for r in results['statuses']:
		tweets.append(r['text'])

	return tweets

