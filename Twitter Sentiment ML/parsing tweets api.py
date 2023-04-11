import tweepy
from tweepy import OAuthHandler

consumer_key = 'a5RMFSKBLcwiKj3izA8YAKBun'
consumer_secret = '3IV3t73y5oiRreZ94eIkRjwxLYpuqqMnbtp0v3A0EEsUyI3QHQ'
access_token = '339161171-DkXMRa3TmYsBXblw3gOLFwK5XaQvDJv9mosxD0Bx'
access_secret = 'hlm2TREyDhrVEXG8xHQBnJkJJDzyd25CwL2IlH99OSlFa'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)
 
api = tweepy.API(auth)


for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)