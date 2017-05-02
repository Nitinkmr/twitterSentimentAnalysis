from django.shortcuts import render
from .getSentiment import getTweets
# Create your views here.
from countries import country_list
from twitter import *
from .forms import NameForm


global percentage
global result




t = Twitter(
    auth=OAuth('2955186811-3knD17GyGB21G1obeECLiMA5NsJTNU1tkeBG94J', 
               '7Ba84Alidfz9nAZWcb33EFW2DmeCyxr9SJoXvVYyEkzDx',
               'UtvgXDJeHGZoL8naPRBVQJBTU',
               'xUO1RzRoIqQBP5pMhiscLBDyRH9cLEUtw8WtgZ9RvFI721MR8I'))

def analyseTweets(tweets):
	 # picking positive tweets from tweets
    
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
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


def searchByUserName(request):

	return render(request, 'searchBy.html', {'searchBy':'userName'})

def getTweetByUserName(request):
	userName = request.GET.get('userName')
	print userName
	return render(request, 'searchBy.html', {'searchBy':'userName'})


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


def countryVisual(request):

    global countryResult

    countryResult['pTweets'] = sorted(countryResult['pTweets'], key=lambda tweet: int(tweet['retweetCount'])  ,reverse=True)
    countryResult['nTweets'] = sorted(countryResult['nTweets'], key=lambda tweet: tweet['retweetCount'],reverse=True)
    
    pTweets = []
    nTweets = []
    for x in range(0,5):
        print result['pTweets'][x]
        try:
            pTweets.append(countryResult['pTweets'][x])
            nTweets.append(countryResult['nTweets'][x])
        except Exception as e:
            print e
    return render(request, 'visualisations.html', {'percentage':percentage,'influentialPTweets':pTweets,'influentialNTweets':nTweets})


def visualisations(request):

    global percentage	
    global result

    print result

    result['pTweets'] = sorted(result['pTweets'], key=lambda tweet: int(tweet['retweetCount'])  ,reverse=True)
    result['nTweets'] = sorted(result['nTweets'], key=lambda tweet: tweet['retweetCount'],reverse=True)
    
    pTweets = []
    nTweets = []
    for x in range(0,5):
        try:
            print result['pTweets'][x]
            
            pTweets.append(result['pTweets'][x])
            nTweets.append(result['nTweets'][x])
        except Exception as e:
          print e    
    print result['pTweets']
    return render(request, 'visualisations.html', {'percentage':percentage,'influentialPTweets':pTweets,'influentialNTweets':nTweets})



 
def country_dropDown(request):
    # if this is a POST request we need to process the form data
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        trending_issues = []
        
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
        
            selected_country = form.cleaned_data['countries_drop_down']    
            
            # get woeid for the country selected

            for country in country_list:
                if country['name'] == selected_country:
                    woeid = country['woeid']
                    break

            # get trending issues
            try:
                result = t.trends.place(_id = woeid,count = 3) 
            except Exception as(e):
                print str(e)

            i = 0
            finalResult = []
            for tweet in result[0]['trends']:
              
               temp = getTweets(tweet['name'])
              
               for x in temp:
                finalResult.append(x)

               trending_issues.append({'tweet':tweet['name'],'index':i})
               i = i+1
               if i == 3:
                break

            global result
            result = []
            result = analyseTweets(finalResult)

            print "result is"
            print result
            global percentage
            percentage = {}
            percentage  ={
                            'pPercent':result['pPercent'],
                            'nPercent':result['nPercent'],
                            'neutraltPercent':result['neutraltPercent']
                         }
            print "\n\n\n\n"

            print percentage
            print "\n\n\n\n"
        else:
            print "error in country selection"
    # if a GET (or any other method) we'll create a blank form
        
       
        return render(request, 'displayCountryTweets.html', {'tweets':finalResult})
    else:
        form = NameForm()  
        print "get"    
    	return render(request, 'selectCountry.html', {'form':form})


    
    

    
