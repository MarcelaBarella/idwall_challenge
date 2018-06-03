# -*- coding: utf-8 -*-
import os
import argparse
import json
import time

import scrapy
from scrapy.crawler import CrawlerProcess
from halo import Halo

from reddit_crawler.spiders.ungoliant import RedditSpider

OUTPUT_PATH = '/app/crawlers/reddit_crawler/output.json'
parser = argparse.ArgumentParser(description='Simple Reddit Crawler')

if os.path.isfile(OUTPUT_PATH):
    os.remove(OUTPUT_PATH)

parser.add_argument('--subreddits',
    nargs='+',
    help='Subreddits that will be crawled. To pass multiples, separate by semicolon',
    required=True)

arguments = parser.parse_args()
subreddits = ';'.join(arguments.subreddits)

spinner = Halo(text='Crawling data from Reddit', spinner='dots')
spinner.start()

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0',
    'FEED_FORMAT': 'json',
    'FEED_URI': OUTPUT_PATH,
    'DOWNLOAD_DELAY': '1',
    'CONCURRENT_REQUESTS': '1',
    'LOG_ENABLED': 'False'
})
process.crawl(RedditSpider, subreddits=subreddits)
process.start()
process.stop()

spinner.stop()

with open(OUTPUT_PATH) as f:
    data = json.load(f)
    print(json.dumps(data, sort_keys=True, indent=2))