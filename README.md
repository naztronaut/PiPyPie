# PiPyPie

A dumb twitter bot that responds to mentions and hashtags. During Pi Day, I'll be giving out one Raspberry Pi Zero W. Tweet at @PiPyPi with #PiDayPiGiveaway and throw your name into the 
pot. 

## Demo

<a href="https://www.youtube.com/watch?v=CvN9X5nqWH0" target="_blank"><img src="PiDayPiGiveaway.jpg" alt="PiPyPie Demo" width="700px" /></a>


## Table of Contents

1. [Getting Started](#getting-started)
2. [The Bot](#the-bot)
    1. [Adding New Hashtags](#adding-new-hashtags)
3. [Authors](#authors)
4. [License](#license)
5. [Questions](#questions-)
6. [Contribute](#contribute)

## Getting Started

This can be run on almost any hardware. I chose to run it on a Raspberry Pi but you can run it on AWS, DigitalOcean, GCP, or just your 
computer. 

## The Bot

### Adding new hashtags

@PiPyPie runs everyminute through a cron job that looks for mentions and hashtags defined in `config.ini`. To add new hashtags to respond to, 
simply edit `config.ini` and add a couple of lines. The first line is the actual HASHTAG:

```editorconfig
HASHTAGS = HAPPYPIDAY,PIDAYHELP,NEWHASHTAGHERE
``` 

Separate the hashtags by comma. They don't have to be all uppercase but I like it leaving it like that. Don't put any spaces. 

Then add a new line with the prefix `PI_DAY_MSG_` followed by your `NEWHASHTAGHERE`:

```editorconfig
PI_DAY_MSG_NEWHASHTAGHERE = put your message right over here
```

And that's all you need. 

The "JOKE" hashtag is special since it doesn't respond with a generic message. If you want to change it, edit that line:

```editorconfig
PI_DAY_JOKE_HASHTAG = PIDAYJOKE
```

If you want to get rid of it, you can either just change the hashtag so that it never matches OR you can comment it out. If you do comment this
out, make sure to comment out the following block on `tweets.py`:

```python
elif hashtag['text'].lower() == cfg['PI_DAY_JOKE_HASHTAG'].lower():
    with open(cfg['JOKES_FILE'], 'r') as f:
        joke = random.choice(f.readlines())
        msg = f"{joke}{cfg['TWEET_END']}"
    break
```

If you don't comment it out, the app may fail trying to read a hashtag that doesn't exist in the config. 

## Authors
* **Nazmus Nasir** - [Nazmus](https://nazm.us) - Owner of EasyProgramming.net

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Questions ?
Have questions? You can reach me through several different channels. You can ask a question in the  [issues forum](/../../issues), 
on [EasyProgramming.net](https://www.easyprogramming.net), or on the video comments on YouTube. 


## Contribute 
I will accept Pull requests fixing bugs or adding new features after I've vetted them. Feel free to create pull requests!  