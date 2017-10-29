"""prebuilt blog bot"""
def prebuild():
    prebuild = """ \nimport feedparser
#pass the api keys
twitter = Twython( CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET )

link = ("%s")

#Parse out the feed
blog = feedparser.parse( link )

# blog title
title = (blog['feed']['title'])

# this grabs the entries title and link
blog_title = (blog['entries'][0]['title'])
blog_link = (blog['entries'][0]['link'])

# build my tweet
tweet = ("%s " + title +" "+ blog_title + " " + blog_link)

# tweet it
twitter.update_status( status=tweet )"""
    return prebuild
