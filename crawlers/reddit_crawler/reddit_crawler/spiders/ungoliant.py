# -*- coding: utf-8 -*-

import scrapy

from reddit_crawler.utils import numerize
from reddit_crawler.items import Thread

class RedditSpider(scrapy.Spider):
    name = 'reddit'

    def __init__(self, subreddits='', *args, **kwargs):
        super(RedditSpider, self).__init__(*args, **kwargs)

        self.urls = []
        for subreddit in subreddits.split(';'):
            self.urls.append('https://www.reddit.com/r/{}/top/?t=week'.format(subreddit))

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.get_most_popular_threads)

    def get_most_popular_threads(self, response):
        threads = response.css('.Post')

        for thread in threads:
            upvotes = thread.css('.s1kggl1x-1.dhcHrX::text').extract()[0]
            upvotes = numerize(upvotes)
            is_promoted = thread.css('.s1p3f9iv-0').extract()
            
            if is_promoted or int(upvotes) < 5000:
                continue

            subreddit = response.url.split('/')[-3]
            thread_title = thread.css('.dmstkr-0::text').extract()[0]
            thread_url = 'https://www.redit.com' + thread.css('.SQnoC3ObvgnGjWt90zD9Z').xpath('@href').extract()[0]
            comments_url = 'https://www.redit.com' + thread.css(".jb5xhx-4").xpath('@href').extract()[0]

            result = Thread()
            result['upvotes'] = int(upvotes)
            result['subreddit'] = subreddit
            result['title'] = thread_title
            result['thread_url'] = thread_url
            result['comments_url'] = comments_url
            yield result


