from .scripts import hashtagfinder
from django.shortcuts import redirect,render

def index(request):
    return render(request, 'twitterscraper/index.html')


def search(request):
    user_input = request.POST['user_hashtag_input']
    request.session['list_of_hashtags'] = hashtagfinder.hashtagfinder(user_input);
    return redirect('/results/')

def results(request):
    hashtags = request.session['list_of_hashtags']
    return render(request, 'twitterscraper/results.html', {'hashtags':hashtags})

def details(request):
	results = request.session['list_of_hashtags']
	user_selected_word = request.POST['user_selected_word']
	details_list = [result for result in results if user_selected_word in result]
	return render(request, 'twitterscraper/details.html', {'details_list':details_list})
