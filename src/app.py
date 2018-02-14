import datetime
import time
import tweepy
import os

PREVIOUS_FOLLOWERS_IDS = []


def check_unfollowers():
    '''
    Checks Twitter unfollowers on every five minutes
    and sends direct message to you.
    '''

    consumer_key = os.environ['CONSUMER_KEY']
    consumer_secret = os.environ['CONSUMER_SECRET']
    access_token = os.environ['ACCESS_TOKEN']
    access_token_secret = os.environ['ACCESS_SECRET']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    my_username = os.environ['USERNAME']

    while True:
        current_followers_ids = fetch_follower_ids(api, my_username)
        global PREVIOUS_FOLLOWERS_IDS
        print("{} Previous followers count:{}, Current followers count:{}"
              .format(datetime.datetime.now(), len(PREVIOUS_FOLLOWERS_IDS), len(current_followers_ids)))

        if PREVIOUS_FOLLOWERS_IDS:
            unfollowers = get_unfollower_ids(current_followers_ids)
            for unfollower in unfollowers:
                user = api.get_user(unfollower)
                message = "@{} unfollowed you.".format(user.screen_name)
                print(message)
                api.send_direct_message(screen_name=my_username, text=message)
        else:
            print("{} Your followers saved.".format(datetime.datetime.now()))

        PREVIOUS_FOLLOWERS_IDS = current_followers_ids
        time.sleep(60 * 5)


def get_unfollower_ids(current_followers_ids):
    '''
    Compares previous and current followers' id
    and finds unfollowers.
    '''
    diff = []
    global PREVIOUS_FOLLOWERS_IDS

    for follower_id in PREVIOUS_FOLLOWERS_IDS:
        if follower_id not in current_followers_ids:
            diff.append(follower_id)
    return diff


def fetch_follower_ids(api, username):
    '''
    Fetches specified username's followers' id
    '''
    followers = []
    print("{} Fetching followers...".format(datetime.datetime.now()))
    for page in tweepy.Cursor(api.followers_ids, screen_name=username).pages():
        followers.extend(page)
    return followers


def main():
    check_unfollowers()


if __name__ == "__main__":
    main()