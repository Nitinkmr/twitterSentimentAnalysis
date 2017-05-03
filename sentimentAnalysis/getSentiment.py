import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from TwitterSearch import *

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console

        consumer_key = 'UtvgXDJeHGZoL8naPRBVQJBTU'
        consumer_secret = 'xUO1RzRoIqQBP5pMhiscLBDyRH9cLEUtw8WtgZ9RvFI721MR8I'
        access_token = '2955186811-3knD17GyGB21G1obeECLiMA5NsJTNU1tkeBG94J'
        access_token_secret = '7Ba84Alidfz9nAZWcb33EFW2DmeCyxr9SJoXvVYyEkzDx'
 
        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")
 
    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
 
    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
 
    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []
        allTexts = []
        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)
            
           # print self.api.statuses.user_timeline(screen_name="billybob")

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
               
                parsed_tweet = {}
 
                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                if tweet.text in allTexts:
                    continue
                else:
                    allTexts.append(tweet.text)
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
               
                parsed_tweet['retweetCount'] =  tweet.retweet_count

                parsed_tweet['url'] = "https://twitter.com/statuses/" + tweet.id_str
                
                #parsed_tweet['profilePic'] = tweet.retweeted_status.user.profile_image_url_https

                #parsed_tweet['userName'] = tweet.retweeted_status.user.name

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
 
            # return parsed tweets
            return tweets
 
        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))
 
def getTweets(searchBy):
    # creating object of TwitterClient Class

#    https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=twitterapi&count=2

    
       
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = searchBy, count = 100)
   # print tweets
    return tweets
    
   
if __name__ == "__main__":
    # calling main function
    main()
