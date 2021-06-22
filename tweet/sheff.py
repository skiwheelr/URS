all
import tweepy, config, users, re, groupy
from tweepy import OAuthHandler
from tweepy import API
print(tweepy.__version__)
auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token,config.access_token_secret)
api = tweepy.API(auth)
from groupy.client import Client
client = Client.from_token(config.groupme_token)

def messenger(msg):
    for group in client.groups.list():
        if group.name=="COMMonMENTions":
            # print(group.name)
            # msg ="Mentioned by pharmdca and mrzackmorris: "+ str(tickr)
            message = group.post(text=msg)

exp = r'🔔'

sheff = []

#sheff
for user in users.list[3:4]:
    userID = user
    tweets = api.user_timeline(screen_name=userID,count=10, include_rts = False, tweet_mode='extended')
    for info in tweets:
        if re.findall(exp,info.full_text):
            print(info.full_text)
            messenger(info.full_text)
