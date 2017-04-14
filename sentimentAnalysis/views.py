from django.shortcuts import render
from .getSentiment import getTweets
# Create your views here.

def firstForm(request):

	return render(request, 'index.html', {})

'''
def searchByCountry(request):

	return render(request, 'index.html', {})

'''

def searchByTweet(request):

	#if request.method == "GET":	 

	return render(request, 'searchBy.html', {'searchBy':'tweet'})


'''def searchByUser(request):
	return render(request, 'index.html', {})
'''
#/(?P<tweet>[0-9]{1})/
def getTweetByTweetName(request):
	#print tweet
	print "reached"
	tweet = request.GET.get('tweet')
	print tweet
	return render(request, 'searchBy.html', {'searchBy':'tweet'})
