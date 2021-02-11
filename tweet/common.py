
import tweepy, config, users, re, groupy
from tweepy import OAuthHandler
from tweepy import API
print(tweepy.__version__)
auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token,config.access_token_secret)
api = tweepy.API(auth)
from groupy.client import Client
client = Client.from_token(config.groupme_token)

def messenger(tickr):
    for group in client.groups.list():
        if group.name=="COMMonMENTions":
            # print(group.name)
            # msg ="Mentioned by pharmdca and mrzackmorris: "+ str(tickr)
            message = group.post(text="Mentioned by @pharmdca and @mrzackmorris: "+ str(tickr))

exp = r'\$([A-Z]{3,4})'

one = []
two = []
both = []

#mrzackmorris
for user in users.list[:1]:
    userID = user
    tweets = api.user_timeline(screen_name=userID,count=20, include_rts = False, tweet_mode='extended')
    for info in tweets:
        if re.findall(exp,info.full_text):
            for ticker in re.findall(exp,info.full_text):
                if ticker not in one:
                    one.append(ticker)
            # print(user, " mentioned ", re.findall(exp,info.full_text))
    print(user, "mentioned", one)
    
#pharmdca
for user in users.list[1:2]:
    userID = user
    tweets = api.user_timeline(screen_name=userID,count=20, include_rts = False, tweet_mode='extended')
    for info in tweets:
        if re.findall(exp,info.full_text):
            for ticker in re.findall(exp,info.full_text):
                if ticker not in two:
                    two.append(ticker)
            # print(user, " mentioned ", re.findall(exp,info.full_text))
    print(user, "mentioned", two)

    for tic in one:
        if tic in two:
            both.append(tic)

print("Both mentioned ", both)
if not both: print("Nothing Notable")
else: messenger(both)
