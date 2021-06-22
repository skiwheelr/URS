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

def check_if_string_in_file(file_name, string_to_search):
    """ Check if any line in the file contains given string """
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if string_to_search in line:
                return True
    return False


#sheff
for user in users.list[3:4]:
    userID = user
    tweets = api.user_timeline(screen_name=userID,count=200, include_rts = False, tweet_mode='extended')
    for info in tweets:
        if re.findall(exp,info.full_text):
            # print(info.full_text)
            file = open("sheffres.txt", 'a+')
            file.close()
            if check_if_string_in_file('sheffres.txt', info.full_text):
                print("already sent")
            else:
                file = open("sheffres.txt", 'a+')
                file.write('\n' + info.full_text + '\n')
                file.close()
                print("new notification")
                messenger(info.full_text)
