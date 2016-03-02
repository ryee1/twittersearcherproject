from twython import Twython

APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

results = twitter.search(q="#warriors", count='100', lang='en', max_id='')
tweets = []
for r in results['statuses']:
	tweets.append(r['text'])

for t in tweets:
	#Used to print to IDLE in Windows 10, will change later.
	encodedtweet = t.encode("utf-8", errors='ignore')
	print(encodedtweet)


