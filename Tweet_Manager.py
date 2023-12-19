from Twitter_Bot import TwitterBot
from config import *
import json


class TweetManager():
    def __init__(self, tweet: str):
        self.bot = self.initialize_bot()
        self.payload = json.dumps({"text": tweet})

    def initialize_bot(self):
        # get the keys from the json file
        with open(AUTHENTICATION_FILE, "r") as file:
            keys = json.load(file)

        # create the bot
        bot = TwitterBot(keys["consumer_key"],
                         keys["consumer_secret"],
                         keys["access_token"],
                         keys["access_token_secret"])
        return bot

    def post_tweet(self):
        self.bot.post_tweet(self.payload)