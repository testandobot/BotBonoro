import os
import tweepy
import time
import datetime
from os import environ

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_KEY = os.environ.get('ACCESS_KEY')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
indice = False
textos = ["Manda salve pro 3s2, Presidente @jairbolsonaro\nSomos fãs do mito", "Somos muito fãs do excelentíssimo Presidente @jairbolsonaro\nManda salve pro 3S2, mito"]
print(api.me())
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        global indice
        if status.user.screen_name == "jairbolsonaro" and not "RT" in status.text:
            try:
                if not indice:
                    api.update_status(textos[0], in_reply_to_status_id=status.id, auto_populate_reply_metadata=True)
                else:
                    api.update_status(textos[1], in_reply_to_status_id=status.id, auto_populate_reply_metadata=True)
                api.create_favorite(status.id)
                api.retweet(status.id)
                indice = not indice
            except tweepy.TweepError as e:
                print(e.reason)        


                    
if __name__ == "__main__":
    while True:
        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
        myStream.filter(follow=["128372940"])
