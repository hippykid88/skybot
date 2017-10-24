#!/usr/bin/python3
#prebuilt hastag_bot
def prebuild():
    prebuild = """ \n#passes the api keys
twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

#setting search results as a variable
bad_words = [" -RT", "nigger", "fuck", "sex", "trump"]
good_words = ('%s')
blacklist = " -".join(bad_words)
keywords = good_words + blacklist
search_results = twitter.search(q=keywords, count=1)
for tweet in search_results["statuses"]:
    try:
        twitter.retweet(id = tweet["id_str"])
    except:
        print('Sorry Dave I failed')"""
    return prebuild


