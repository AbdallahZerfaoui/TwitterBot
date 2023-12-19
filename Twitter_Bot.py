import requests
from requests_oauthlib import OAuth1

class TwitterBot:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        # OAuth 1.0a User Context authentication
        self.auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)

        # The URL for creating a tweet
        self.url = "https://api.twitter.com/2/tweets"

        # Headers
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        }

    def post_tweet(self, payload):
        # Making the POST request to Twitter API
        response = requests.post(self.url,
                                 headers=self.headers,
                                 data=payload,
                                 auth=self.auth)

        # Checking the response
        if response.status_code == 201:
            print("Successfully posted the tweet.")
            print(response.json())
        else:
            print(f"Failed to post tweet: {response.status_code}")
            print(response.json())


