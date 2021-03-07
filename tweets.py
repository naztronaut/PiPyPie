import tweepy
import random
import configparser
from twitter_auth import twitter_api as api

# Read config files - default config and auth config
config = configparser.ConfigParser()
config.read('config.ini')
cfg = config['DEFAULT']


# Store id of the last mentioned tweet so that you don't double-reply
def update_last_mentioned_tweet(tweet_id):
    with open("timeline_since.txt", "w") as file:
        file.write(str(tweet_id))


with open("timeline_since.txt", 'r') as f:
    since_tweet_id = f.readline()
    if since_tweet_id == '':
        since_tweet_id = api().mentions_timeline(count=1)[0].id
        update_last_mentioned_tweet(since_tweet_id)

# tweets = tweepy.Cursor(api.mentions_timeline, since_id=since_tweet_id, tweet_mode='extended').items(20)

if __name__ == "__main__":
    tweets = api().mentions_timeline(since_id=since_tweet_id, tweet_mode='extended', count=20)
    for tweet in reversed(tweets):
        hashtags = (tweet._json['entities']['hashtags'])
        msg = ''
        for hashtag in hashtags:
            for config_hashtag in cfg['HASHTAGS'].split(','):
                if config_hashtag.lower() == hashtag['text'].lower():
                    msg = cfg['PI_DAY_MSG_' + config_hashtag]
                    break
                elif hashtag['text'].lower() == cfg['PI_DAY_JOKE_HASHTAG'].lower():
                    with open(cfg['JOKES_FILE'], 'r') as f:
                        joke = random.choice(f.readlines())
                        msg = f"{joke}{cfg['TWEET_END']}"
                    break
        if msg != '':
            try:
                api().update_status(msg, in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
                print(f"Tweeted to {str(tweet.id)}: {msg}")
            except Exception as e:
                print(tweet.id)
                print(e)
        else:
            print("nothing to tweet")

        # Store the tweet id in the file so that it's skipped next time
        update_last_mentioned_tweet(tweet.id)
