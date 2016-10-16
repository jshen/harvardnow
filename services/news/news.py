import json
import tweepy

#############################
##    News Function     ##
#############################

def getTweet():

    auth = tweepy.OAuthHandler('H0lyUTJinTalk6gR6zRtU3Jf8', 'DY0b8zDZd3MNRLXH8N1erz8S4wjmVDJmu6aSwIfygbxVtnNRIT')
    auth.set_access_token('2430849618-lqsi9TTYKgi0mRY62HodyBV5EvX5Gv98D3MAPYj', '0o2Z30ifHfhBzbNMKw7cq33exAkLYiJDlpqjZ4feoRLlH')

    api = tweepy.API(auth)
    user_tweets = api.user_timeline('Harvard')

    return user_tweets[0].text

special = 'A service that returns the latest Harvard University tweet.'

def eval():
    return getTweet()