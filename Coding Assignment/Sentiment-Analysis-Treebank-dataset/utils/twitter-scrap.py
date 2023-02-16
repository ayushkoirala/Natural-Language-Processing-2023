import snscrape
import snscrape.modules.twitter as sntwitter
import pandas as pd
import itertools
raw_content = []
result = sntwitter.TwitterHashtagScraper('macbook_2022').get_items()
counter = 0
for i, tweet in enumerate(result):
    if(tweet.lang == 'en'):
        print(tweet.rawContent)
        counter += 1
        if counter > 50:
            break
