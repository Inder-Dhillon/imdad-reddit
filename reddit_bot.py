import praw
from os import environ
import requests
import time

reddit = praw.Reddit(client_id=environ['REDDIT_ID'],
                     client_secret=environ['REDDIT_SECRET'],
                     password=environ['REDDIT_PASSWORD'],
                     user_agent='imdad',
                     username='imdad_bot')

subreddit = reddit.subreddit("all")  # subreddits

for comment in subreddit.stream.comments():
    if reddit.user.me() != comment.author.name:
        comment_lower = comment.body.lower()
        comment_lower_list = comment_lower.split(" ")
        try:
            if "im" in comment_lower_list:
                trigger_loc = comment_lower.find("im ") + 3
                end_loc = comment_lower.find(".", trigger_loc)
                if end_loc == -1:
                    end_loc = comment_lower.find("\n", trigger_loc)
                    if end_loc == -1:
                        comment.reply("Hi " + comment.body[trigger_loc:]+ ", I'm Dad👨")
                    else:
                        comment.reply("Hi " + comment.body[trigger_loc:end_loc] + ", I'm Dad👨")
                else:
                    comment.reply("Hi " + comment.body[trigger_loc:end_loc] + ", I'm Dad👨")
            elif "i'm" in comment_lower_list:
                trigger_loc = comment_lower.find("i'm ") + 4
                end_loc = comment_lower.find(".", trigger_loc)
                if end_loc == -1:
                    end_loc = comment_lower.find("\n", trigger_loc)
                    if end_loc == -1:
                        comment.reply("Hi " + comment.body[trigger_loc:] + ", I'm Dad👨")
                    else:
                        comment.reply("Hi " + comment.body[trigger_loc:end_loc] + ", I'm Dad👨")
                else:
                    comment.reply("Hi " + comment.body[trigger_loc:end_loc] + ", I'm Dad👨")
            else:
                requests.get(url='https://imdadbot.herokuapp.com/')
                time.sleep(300)


        except:
            pass