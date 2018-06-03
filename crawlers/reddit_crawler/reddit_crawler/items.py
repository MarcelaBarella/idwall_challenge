# -*- coding: utf-8 -*-

import scrapy


class Thread(scrapy.Item):
    upvotes = scrapy.Field()
    subreddit = scrapy.Field()
    title = scrapy.Field()
    thread_url = scrapy.Field()
    comments_url = scrapy.Field()
