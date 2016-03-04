from .scripts import hashtagfinder
from .scripts import tweetRetriever
from django.shortcuts import redirect,render

def index(request):
    return render(request, 'twitterscraper/index.html')


def search(request):
    user_input = request.POST['user_hashtag_input']
    request.session['list_of_tweets'] = tweetRetriever.tweetRetriever(user_input);
    return redirect('/results/')

def results(request):
    fulltweets = request.session['list_of_tweets']
    tweets = []
    for t in fulltweets:
    	tweets.append(t['tweet'])
    return render(request, 'twitterscraper/results.html', {'tweet':tweets})

def tableresults(request):
	results = request.session['list_of_tweets']
	return render(request, 'twitterscraper/tableresults.html', {'results':results})
