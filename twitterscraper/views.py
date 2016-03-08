from .scripts import tweetRetriever
from django.shortcuts import redirect,render

def index(request):
    return render(request, 'twitterscraper/index.html')

def search(request):
    user_input = request.POST['user_hashtag_input']
    list_of_tweets = tweetRetriever.tweetRetriever(user_input)
    request.session['list_of_tweets'] = list_of_tweets

    return redirect('/results/')

def results(request):
    fulltweets = request.session['list_of_tweets']
    tweets = []
    for t in fulltweets:
    	for word in t['tweet'].split():	
	    	if not word.isalnum():
	    		continue
    		tweets.append(word)
    return render(request, 'twitterscraper/results.html', {'tweet':tweets})

def tableresults(request):
	results = request.session['list_of_tweets']
	return render(request, 'twitterscraper/tableresults.html', {'results':results})

def details(request):
	results = request.session['list_of_tweets']
	user_selected_word = request.POST['user_selected_word']
	details_list = [result['tweet'] for result in results if user_selected_word in result['tweet'].split()]
	return render(request, 'twitterscraper/details.html', {'details_list':details_list})
