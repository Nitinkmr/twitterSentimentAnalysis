from django.shortcuts import render
from .getSentiment import getTweets
# Create your views here.

global percentage
global result

def analyseTweets(tweets):
	 # picking positive tweets from tweets
    
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    print ptweets
    # percentage of positive tweets
   # print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
    
    neutralTweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']

    global result
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
	
	global result
	result = []
	result = analyseTweets(tweets)
	
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

	global percentage	
	global result

	print result

	result['pTweets'] = sorted(result['pTweets'], key=lambda tweet: int(tweet['retweetCount'])	,reverse=True)
	result['nTweets'] = sorted(result['nTweets'], key=lambda tweet: tweet['retweetCount'],reverse=True)
	
	pTweets = []
	nTweets = []
	for x in range(0,5):
		print result['pTweets'][x]
		pTweets.append(result['pTweets'][x])
		nTweets.append(result['nTweets'][x])

	print result['pTweets']
	return render(request, 'visualisations.html', {'percentage':percentage,'influentialPTweets':pTweets,'influentialNTweets':nTweets})


