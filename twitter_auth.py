import configparser
import tweepy

# Read auth config file
auth_config = configparser.ConfigParser()
auth_config.read('auth.ini')
auth_cfg = auth_config['DEFAULT']


auth = tweepy.OAuthHandler(auth_cfg['CONSUMER_KEY'], auth_cfg['CONSUMER_SECRET'])
# Set access token
auth.set_access_token(auth_cfg['ACCESS_TOKEN'], auth_cfg['ACCESS_SECRET'])

# Construct the API instance
api = tweepy.API(auth)

try:
    api.verify_credentials()
except Exception as e:
    print("Error during authentication")
    print(e)


def twitter_api():
    return api
