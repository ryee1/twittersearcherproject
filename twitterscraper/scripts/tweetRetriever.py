from twython import Twython

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
		temp = {'username':r['user']['screen_name'], 'date':r['created_at'], 'tweet':r['text']}
		tweets.append(temp)
	return tweets


