import tweepy
import random
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
cfg = config['DEFAULT']

auth_config = configparser.ConfigParser()
auth_config.read('auth.ini')
acfg = auth_config['DEFAULT']


auth = tweepy.OAuthHandler(acfg['CONSUMER_KEY'], acfg['CONSUMER_SECRET'])
# Redirect user to Twitter to authorize

# Get access token
auth.set_access_token(acfg['ACCESS_TOKEN'], acfg['ACCESS_SECRET'])

# Construct the API instance
api = tweepy.API(auth)
try:
    api.verify_credentials()
except:
    print("Error during authentication")

# print(api.me().screen_name)
# print(api.home_timeline(1))

# for tweet in api.home_timeline(1):
#     print(tweet.id)
# api = tweepy.API(auth)
#
# for tweet in tweepy.Cursor(api.search, q='python').items(1):
    # print(tweet._json['text'])
    # print(tweet.retweeted)
    # print(api.get_status(tweet.id, tweet_mode='extended')._json['full_text'])
    # try:
    #     if not tweet.retweeted:
    #         api.retweet(tweet.id)
    # except:
    #     print('already retweeted')
with open("timeline_since.txt", 'r') as f:
    since_tweet_id = f.readline()
    # print(since_tweet_id)
    if since_tweet_id == '':
        since_tweet_id = api.mentions_timeline(count=1)[0].id
        with open("timeline_since.txt", "w") as f1:
            f1.write(str(since_tweet_id))


# for hashtag in cfg['HASHTAGS'].split(','):
#     print(hashtag)
#     if hashtag.lower() ==

# tweets = tweepy.Cursor(api.mentions_timeline, since_id=since_tweet_id, tweet_mode='extended').items(20)
tweets = api.mentions_timeline(since_id=since_tweet_id, tweet_mode='extended', count=20)
for tweet in reversed(tweets):
    # print(tweet._json)
    hashtags = (tweet._json['entities']['hashtags'])
    msg = ''
    for hashtag in hashtags:
        for config_hashtag in cfg['HASHTAGS'].split(','):
            if config_hashtag.lower() == hashtag['text'].lower():
                msg = cfg['PI_DAY_MSG_' + config_hashtag]
                break
            elif hashtag['text'].lower() == "pidayjoke":
                with open('jokes.txt', 'r') as f:
                    joke = random.choice(f.readlines())
                    msg = f"{joke}{cfg['TWEET_END']}"
                break

        # if hashtag['text'].lower() == "pidayhelp":
        #     msg = cfg['PI_DAY_HELP_MSG']
        #     break
        # elif hashtag['text'].lower() == "happypiday":
        #     msg = cfg['HAPPY_PI_DAY_MSG']
        #     break
        # elif hashtag['text'].lower() == "pidayjoke":
        #     with open('jokes.txt', 'r') as f:
        #         joke = random.choice(f.readlines())
        #         msg = f"{joke}{cfg['TWEET_END']}"
        #     break

    if msg != '':
        try:
            api.update_status(msg, in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
            print("Tweeted: " + msg)
            print("Tweet Id: ")
            print(tweet.id)
            with open("timeline_since.txt", "w") as f:
                f.write(str(tweet.id))
        except Exception as e:
            print(tweet.id)
            print(e)

    else:
        print("nothing to tweet")

# print(api.mentions_timeline())


# api.update_status("Hello from an API")
