"""
Do you think you're informed on CryptoTwitter? When trading in your portfolio, why not just sit and scroll Twitter like you already do? Introducing, Hummscroller.

This module checks on your 100 latest liked tweets and pulls out any cashtags like $BTC.

The assumption is that if you liked a tweet promoting an asset, you agreed with it. However, if the tweet sentiment was negative, it would mean you agreed that the asset isn't good.

This data gets written into a trading strategy using Hummingbot scripts. It creates buy orders for tokens you agreed with, and sells them 24 hours later. It keeps a rolling list of your own sentiment on assets. This list is used to build buy and sell orders.

Buys will be weighted by the amounts of likes and retweets you do. Liking a negative sentiment one will reduce the weight.

Resources:
- https://hummingbot.notion.site/How-to-Create-a-Script-b789c9fe1f97492cbc4673ae0ed55632
- https://hummingbot.org/global-configs/telegram/#setting-up-in-hummingbot
- https://shard-watcher-5b5.notion.site/Hummingbot-ETHPortland-Hub-ecfcef0f69234e228d8409453aab2cd7
"""

import tweepy
import re
import os
import json

class HummScroller(object):

    def __init__(self, twitter_bearer_token, twitter_handle):
        self.twitter_bearer_token = twitter_bearer_token
        self.twitter_handle = twitter_handle

        # self.recent_tweet_likes()

    def cashtag_finder(self, string):
        cashtags = re.findall(r'\$[a-zA-Z]+', string)
        return cashtags

    def recent_tweet_likes(self):

        # Initializing the Tweepy client
        client = tweepy.Client(self.twitter_bearer_token)
        auth = tweepy.OAuth2BearerHandler(self.twitter_bearer_token)
        api = tweepy.API(auth)
        user = api.get_user(screen_name = self.twitter_handle)
        twitter_id = user.id

        # See more calls at https://github.com/tweepy/tweepy/tree/master/examples/API_v2
        tweets = client.get_liked_tweets(id=twitter_id, max_results=100)

        # ToDo: classify by sentiment. If you like something negative, it could mean you're bearish on it.
        likes_per_token = {}

        for tweet in tweets.data:
            # print(tweet.text)
            bullish = self.cashtag_finder(tweet.text)
            if len(bullish) > 0:
                # print(tweet.text)
                for tkn in bullish:
                    tkn = tkn.upper()
                    if tkn not in likes_per_token:
                        likes_per_token[tkn] = 1
                    else:
                        likes_per_token[tkn] += 1

        print(json.dumps(likes_per_token, indent=4))
        with open('recent_tweet_likes.json', 'w') as outfile:
            json.dump(likes_per_token, outfile)

if __name__ == "__main__":

    # Environment Variables, or Passed in from TelegramBot?
    TWITTER_HANDLE = os.getenv('TWITTER_HANDLE')
    TWITTER_API_BEARER = os.environ.get('TWITTER_API_BEARER')

    print("Getting cashtags from liked tweets for", "@" + TWITTER_HANDLE)

    HummScroller(TWITTER_API_BEARER, TWITTER_HANDLE).recent_tweet_likes()
