from config import *
import pandas as pd


def get_best_domaines_of_the_day(top : int =10):
    data = pd.read_csv(DOMAINS_DATA_PATH)
    data = data.sort_values(by=["marketplaces"], ascending=False)
    return data.head(top)

def build_a_tweet(top : int =10):
    data = get_best_domaines_of_the_day(top)
    with open("tweet_template.txt", 'r', encoding='utf-8') as file:
        tweet = file.read()
    tweet = tweet.replace("10", str(NBR_OF_TOP_DOMAINS))
    for index, row in data.iterrows():
        tweet += f"{row['domains']} : {row['valuations']}$\n"
    return tweet