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

def messenger(tickr):
    for group in client.groups.list():
        if group.name=="COMMonMENTions":
            # print(group.name)
            # msg ="Mentioned by pharmdca and mrzackmorris: "+ str(tickr)
            message = group.post(text="(<50 Tweets) Mentioned by @ripster47, @pharmdca and @mrzackmorris: "+ str(tickr))

exp = r'\$([A-Z]{3,4})'

one = []
two = []
three = []
all = []

#mrzackmorris
for user in users.list[:1]:
    userID = user
    tweets = api.user_timeline(screen_name=userID,count=100, include_rts = False, tweet_mode='extended')
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
    tweets = api.user_timeline(screen_name=userID,count=100, include_rts = False, tweet_mode='extended')
    for info in tweets:
        if re.findall(exp,info.full_text):
            for ticker in re.findall(exp,info.full_text):
                if ticker not in two:
                    two.append(ticker)
            # print(user, " mentioned ", re.findall(exp,info.full_text))
    print(user, "mentioned", two)

    #ripster47
    for user in users.list[2:3]:
        userID = user
        tweets = api.user_timeline(screen_name=userID,count=100, include_rts = False, tweet_mode='extended')
        for info in tweets:
            if re.findall(exp,info.full_text):
                for ticker in re.findall(exp,info.full_text):
                    if ticker not in three:
                        three.append(ticker)
                # print(user, " mentioned ", re.findall(exp,info.full_text))
        print(user, "mentioned", three)

a_set = set(one)
b_set = set(two)
c_set = set(three)

if (a_set & b_set & c_set):
    all.append(a_set & b_set & c_set)
    print("All 3 mentioned ", all)
    messenger(all)
else: print("Nothing Notable")
