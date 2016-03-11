from twython import Twython
import time

APP_KEY = 'f1HlAsbabsoi3cr5EC3t1NzDH'
APP_SECRET = 'XSsoDYC4W1g2l3VUyU1vtTQ7SroB0olzDokpwD5CpgcRjMh715'
OAUTH_TOKEN = '4760974394-ThpCcbIXGznm51P9RO2jjSsDdjWs8PHYkALk1KD'
OAUTH_TOKEN_SECRET = 'DFkoR2HMhImpfhoTNc3T7WNItqpxfxaE0ciwrFJj500Sd'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

#Uses Twython and Twitter API to grab tweets with the entered word from index
#Adds username, date, and tweet into a list and returns a list containing all
def tweetRetriever(word):
	results = twitter.search(q="#"+word, count='1500', lang='en')
	tweets = []
	for r in results['statuses']:
		t = r['created_at']
		date = t[3:10] + " " +  t[25:]
		temp = {'username':r['user']['screen_name'], 'date':date , 'tweet':r['text'], 'picture_url':r['user']['profile_image_url_https'], 'name':r['user']['name']}
		tweets.append(temp)
	return tweets

