from twython import Twython

APP_KEY = '7CnB7vjanuoSYCS1txkery633'
APP_SECRET = 'kCRmRbS61MENH70dS3eTIkDvgSmqoFXBoOGmtIvlQsfgnbpmdA'
OAUTH_TOKEN = '218601321-r3zVuvxviq48GhHyJGh2q8un2GTsPdIv3Dn8mi6J'
OAUTH_TOKEN_SECRET = 'UmXwih01oeXKnpW9dTqYO3UkRwZCY1Aj3rki0U6Wbxcvh'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def hashtagfinder(word):
	results = twitter.search(q=word, count='100', lang='en')
	tweets = []
	for r in results['statuses']:
		tweets.append(r['text'])

	return tweets

