# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import Request
from lyricsCrawler.items import LyricscrawlerItem
# from lyricsCrawler.youtube_search import youtubeSearch, storeResults

class MetrolyricsSpider(CrawlSpider):
    name = 'metrolyrics'
    allowed_domains = ['metrolyrics.com']
    start_urls = ['http://metrolyrics.com']
    rules = (Rule(link_extractor=LinkExtractor(deny_domains=('google.com'), allow=('artist')), callback='parse_alphabet', follow=True),)

    def parse_alphabet(self, response):
        artists = response.xpath('//*[@class="songs-table"]/tbody/tr/td/a/@href').extract()
        if (artists):
            for artist in artists:
                yield Request(artist, callback=self.parse_artist)
        next_page_url = response.xpath('//*[@class="button next"]/@href').extract_first()
        if (next_page_url):
            yield Request(next_page_url, callback=self.parse_alphabet)

    def parse_artist(self, response):
        songs = response.xpath('//*[@id="popular"]//*[@class="songs-table compact"]/tbody/tr/td/a/@href').extract()
        if (songs):
            for song in songs:
                yield Request(song, callback=self.parse_song)
        next_page_url = response.xpath('//*[@class="button next"]/@href').extract_first()
        if (next_page_url):
            yield Request(next_page_url, callback=self.parse_artist)

    def parse_song(self, response):
        artist = response.xpath('//*[@class="banner-heading"]/h2/a/text()').extract_first()
        title = response.xpath('//*[@class="banner-heading"]/h1/text()').extract_first().replace('Lyrics', '').replace('-', '').replace(artist, '').strip()
        lyrics = ''.join(response.xpath('//*[@class="verse"]/text()').extract())
        url = response.request.url

        if ((lyrics and lyrics.strip) and (title and title.strip) and (artist and artist.strip)):
            item = LyricscrawlerItem()

            item['song_artist'] = artist
            item['song_title'] = title
            item['song_lyrics'] = lyrics
            item['song_url'] = url

            # # retrive popularity and freshness measurements from youtube api
            # query = item['song_title'] + ' ' + item['song_artist']
            # response = youtubeSearch(query)
            # results = storeResults(response)

            # # most relevant video publish date
            # item['song_publish_date'] = results['publishDate'][0]
            # # average views from top 3 relevant videos
            # item['song_views'] = (results['viewCount'][0] + results['viewCount'][1] + results['viewCount'][2]) / 3
            # # average likes from top 3 relevant videos
            # item['song_likes'] = (results['likeCount'][0] + results['likeCount'][1] + results['likeCount'][2]) / 3
            # # average dislike from top 3 relevant videos
            # item['song_dislikes'] = (results['dislikeCount'][0] + results['dislikeCount'][1] + results['dislikeCount'][2]) / 3
            # # average favorites from top 3 relevant videos
            # item['song_favorites'] = (results['favoriteCount'][0] + results['favoriteCount'][1] + results['favoriteCount'][2]) / 3
            # # aggregate tags from top 3 relevant videos
            # tag_list = results['tags'][0] + results['tags'][1] + results['tags'][2]
            # item['song_tags'] = set(tag_list)
            return item