"""
    Twitter bot for sending a random quote to a random user on twitter

    Input:
        Twitter API Authorization info in a json file
        Arg File which specifies the users to possibly dm
        Quote file to grab a random quote from to send to a user

    Main function will grab all arguments then send info to proper functions to get bot arguments.
    We will then loop with a sleep, sending out a random quote to a random user on twitter
"""
import json
import sys
import random
import time
import tweepy

def auth_setup(auth_file):
    """ Opens auth file and grabs all required information for tweepy auth object, return object """

    with open(auth_file) as data_file:
        data = json.load(data_file)

    consumer_key = data["consumer_key"]
    consumer_secret = data["consumer_secret"]
    access_token = data["access_token"]
    access_token_secret = data["access_token_secret"]

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return auth

def get_tweet(in_file):
    """ Open up input file read all quotes into a list, return random quote """

    possible = []
    for tweet in in_file.read().split("DELIM"):
        possible.append(tweet.strip())

    return random.choice(possible)

def get_random_user(in_file):
    """ Open up user input json and grab a random user from the specified users """

    with open(in_file) as data_file:
        data = json.load(data_file)

    users = data["dm_users"]

    return random.choice(users)

def main():
    """ Main function, grab arugments, grab dm arguments, on a loop send dm """

    auth_file = sys.argv[1]
    arg_file = sys.argv[2]
    quote_file = sys.argv[3]

    auth = auth_setup(auth_file)
    api = tweepy.API(auth)

    while True:
        time.sleep(3000)
        user = get_random_user(arg_file)
        tweet = get_tweet(open(quote_file, "r"))

        try:
            api.send_direct_message(user=user, text=tweet)
        except tweepy.TweepError as error:
            print(error)
            continue

if __name__ == "__main__":
    main()
