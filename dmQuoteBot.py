import tweepy
import json
import sys
import random
import time

def auth_setup(authFile):
    
    with open(authFile) as data_file:
        data = json.load(data_file)

    consumer_key = data["consumer_key"]
    consumer_secret = data["consumer_secret"]
    access_token = data["access_token"]
    access_token_secret = data["access_token_secret"]
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return auth

def get_friends(api, user, depth):

    if depth == 1:
        return []
    user = api.get_user(user)
    ret = user.friends()
    for user in user.friends():
        ret += get_friends(api, user, depth +1)
    return ret


def get_tweet(inFile):

    possible = []
    for tweet in inFile.read().split("DELIM"):
        possible.append(tweet.strip())

    return random.choice(possible)


def get_random_user(inFile):

    with open(inFile) as data_file:
        data = json.load(data_file)

    users = data["dm_users"]

    return random.choice(users)    
    
def main():

    authFile = sys.argv[1]
    argFile = sys.argv[2]
    quoteFile = sys.argv[3]

    auth = auth_setup(authFile)
    api = tweepy.API(auth)

    while True:


        user = get_random_user(argFile)
        tweet = get_tweet(open(quoteFile, "r"))

        try:
            api.send_direct_message(user=user, text=tweet)
        except TweepError as e: 
            continue

        time.sleep(300)


if __name__ == "__main__":
    main()
