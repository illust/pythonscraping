# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from scrapy import Item, Field


class WeiboItem(Item):

    id = Field()
    content = Field()
    forward_count = Field()
    comment_count = Field()
    like_count = Field()
    posted_at = Field()
    url = Field()
    user = Field()
