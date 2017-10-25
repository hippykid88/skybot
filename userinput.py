#!/usr/bin/python3.4
############################################################
#                                                          #
# This is Skybot -used to easily deploy new twitter bots   #
# Created by Cory Smith '17                                #
#                                                          #
############################################################
#Import all appropriate files.
import apikeys
import prebuilt_blog
import prebuilt_hashtag
import getpass
import os
from crontab import CronTab


#Define the name of the new Bot
def name_of_tweet():
    print('What do you want to name this bot?: ')
    global bot_name_input
    bot_name_input = input() + '.py'
    name_of_tweet = open(bot_name_input ,'w')
    return name_of_tweet


#This builds the header of the file
def file_header():
    header="#!/usr/bin/python3.4 \n#twitterbot By Skybot! \nfrom twython import Twython \n"
    return header

#function to build a retweet bot
def hashtag_bot ():
    hashtag = input( 'What is the hashtag we are retweeting?: ' )
    hashtag_bot = (prebuilt_hashtag.prebuild() % (hashtag))
    return hashtag_bot

#function to build a blog bot
def blog_bot ():
    link = input( 'What is the rss link you want to tweet about?: ' )
    hashtag = input( 'What #would you like to tweet with it?: ' )
    blog_bot = (prebuilt_blog.prebuild() % (link, hashtag))
    return blog_bot

#Determines what type of bot we make
def type_of_bot():
    bot_type = input('What type of bot is this? retweet or blog?: ').lower()
    if bot_type == "retweet":
        type_of_bot = hashtag_bot()
        return type_of_bot
    elif bot_type == "blog":
        type_of_bot = blog_bot()
        return type_of_bot
    else:
        print('try again')

#This will build the actual bot
def build_a_bot():
    bot_name = name_of_tweet()
    bot_name.write(file_header())
    bot_name.write(apikeys.keys())
    bot_name.write(type_of_bot())
    bot_name.close()

build_a_bot()
print('Bot built now working on setting up the cron job')

#Build the cronjob for the bot

def crontab():
    minute = int(input( 'what minute on the hour do you want this to run?(pick 1-60): ' ))
    hour = int(input( 'what hour would you like this to run(pick from 1-24)?: ' ))
    path = os.getcwd() + "/" + bot_name_input
    username = getpass.getuser()  # grabs username to run cron under
    my_cron = CronTab( user=username )
    job = my_cron.new( command=path)
    job.minute.on( minute )
    job.hour.on( hour )
    my_cron.write()
    os.chmod(path, 744)
    return crontab

crontab()
print('cronjob has been built and you are all done')
