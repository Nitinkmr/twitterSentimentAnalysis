from django.shortcuts import render
from .getSentiment import getTweets
# Create your views here.

global percentage


def analyseTweets(tweets):
	 # picking positive tweets from tweets
    
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
   # print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
    
    neutralTweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']

    result = {
 				'pTweets' : ptweets,
 				'nTweets' :ntweets,
 				'neutralTweets' : neutralTweets,
 				'pPercent' : 100*len(ptweets)/len(tweets),
 				'nPercent' :100*len(ntweets)/len(tweets),
 				'neutraltPercent':100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)
 			}

    #print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
    # percentage of neutral tweets
   # print("Neutral tweets percentage: {} % ".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)))

    return result
	
    
def firstForm(request):

	return render(request, 'index.html', {})

def searchByCountry(request):

	return render(request, 'index.html', {})


def searchByTweet(request):

	#if request.method == "GET":	 

	return render(request, 'searchBy.html', {'searchBy':'tweet'})


def searchByUser(request):
	return render(request, 'index.html', {})



def getTweetByTweetName(request):
	tweet = request.GET.get('tweet')
	tweets = getTweets(tweet)
	result = analyseTweets(tweets)

	#print result['neutralTweets']
	#print result['pTweets']
	global percentage
	percentage = {}
	percentage	={
					'pPercent':result['pPercent'],
					'nPercent':result['nPercent'],
					'neutraltPercent':result['neutraltPercent']
				 }
	return render(request, 'displayTweets.html', {'pTweets':result['pTweets'],'nTweets':result['nTweets'],'neutralTweets':result['neutralTweets'],
				'pPercent':result['pPercent'],'nPercent':result['nPercent'],'neutraltPercent':result['neutraltPercent']		})


def visualisations(request):

	
	return render(request, 'visualisations.html', {'percentage':percentage})