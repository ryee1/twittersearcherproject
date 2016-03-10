from twython import Twython
from .scripts import Tweet

APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

#Uses Twython and Twitter API to grab tweets with the entered word from index
#Adds username, date, and tweet into a list and returns a list containing all
def tweetRetriever(word):
	results = twitter.search(q=word, count='100', lang='en', result_type='recent')
	tweets = []
	for r in results['statuses']:
		tweets.append([Tweet(r['user']['screen_name'], r['created_at'], r['text'])])
	return tweets
