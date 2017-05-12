import tweepy
import json
import sys
import random

def auth_setup():
    
    with open("auth_info.json") as data_file:
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

def main():

    auth = auth_setup()
    api = tweepy.API(auth)

    filename = sys.argv[1]
    tweet = get_tweet(open(filename, "r"))
    api.send_direct_message(user='TylerOrlando28', text=tweet)

if __name__ == "__main__":
    main()
