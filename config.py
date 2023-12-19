from datetime import datetime

AUTHENTICATION_FILE = 'authentication_keys.json'
DOMAINS_DATA_PATH = \
    f'../ExpiredDomains/results/domains_{datetime.now().strftime("%Y-%m-%d")}_final.csv'

NBR_OF_TOP_DOMAINS = 3
MAX_TWEET_LENGTH = 249