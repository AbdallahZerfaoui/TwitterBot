from Tweet_Manager import TweetManager
from utils import *


def main():
    # build the tweet
    tweet = build_a_tweet(top=NBR_OF_TOP_DOMAINS)

    # create the tweet manager
    tweet_manager = TweetManager(tweet)

    # post the tweet
    if len(tweet) <= MAX_TWEET_LENGTH:
        tweet_manager.post_tweet()
    else:
        print("The tweet is too long to be posted. its length is : ", len(tweet))


if __name__ == "__main__":
    #main()
    tweet = build_a_tweet(top=NBR_OF_TOP_DOMAINS)
    print(tweet)
