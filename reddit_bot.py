import praw
from os import environ
import requests

reddit = praw.Reddit(client_id='8x40fzSw4dfW4g',
                     client_secret='ky1QQGeALXm9TFYguOEs271WoWQ',
                     password='asd?8300',
                     user_agent='imdad',
                     username='imdad_bot')
subreddit = reddit.subreddit("all")  # subreddits

for comment in subreddit.stream.comments():
    comment_lower = comment.body.lower()
    comment_lower_list = comment_lower.split(" ")
    try:
        if "im" in comment_lower_list:
            comment.reply("Hi " + comment_lower_list[comment_lower_list.index("im") + 1].replace(",","") + ", I'm Dad👨")
        elif "i'm" in comment_lower_list:
            comment.reply("Hi " + comment_lower_list[comment_lower_list.index("i'm") + 1].replace(",","") + ", I'm Dad👨")
    except:
        requests.get(url='https://imdadbot.herokuapp.com/')
        pass