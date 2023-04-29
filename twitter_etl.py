# %%
import tweepy as t
import pandas as pd
import json
from datetime import datetime
import s3fs
import secret as s

access_key = s.access_key
access_secret = s.access_secret
consumer_key = s.consumer_key
consumer_secret = s.consumer_secret

# Twitter authentication
auth = t.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)

# Create an API object
api = t.API(auth)

tweets = api.user_timeline(screen_name='@elonmusk',
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           # Keep full_text
                           tweet_mode = 'extended'
                           )
print(tweets)