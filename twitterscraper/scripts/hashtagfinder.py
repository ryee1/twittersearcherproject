from twython import Twython

APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def hashtagfinder(word):
	results = twitter.search(q=word, count='100', lang='en')
	tweets = []
	for r in results['statuses']:
		tweets.append(r['text'])

	return tweets

