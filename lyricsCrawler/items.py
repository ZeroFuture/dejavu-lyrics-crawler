# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LyricscrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    song_title = scrapy.Field()
    song_artist = scrapy.Field()
    song_lyrics = scrapy.Field()
    song_url = scrapy.Field()
    # song_publish_date = scrapy.Field()
    # song_views = scrapy.Field()
    # song_likes = scrapy.Field()
    # song_dislikes = scrapy.Field()
    # song_favorites = scrapy.Field()
    # song_tags = scrapy.Field()
