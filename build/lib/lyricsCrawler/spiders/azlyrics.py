# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from lyricsCrawler.items import LyricscrawlerItem

class AzlyricsSpider(scrapy.Spider):
    name = 'azlyrics'
    allowed_domains = ['azlyrics.com']
    start_urls = ['https://www.azlyrics.com/']

    def parse(self, response):  
        alphabet = response.xpath('//*[@class="btn btn-menu"]/@href').extract()
        for c in alphabet:
            yield Request('https:' + c, callback=self.parse_alphabet)

    def parse_alphabet(self, response):
        artists = response.xpath('//*[@class="col-sm-6 text-center artist-col"]//@href').extract()
        if (artists):
            for artist in artists:
                yield Request('https://www.azlyrics.com/' + artist, callback=self.parse_artist)

    def parse_artist(self, response):
        songs = response.xpath('//*[@class="listalbum-item"]//@href').extract()
        if (songs):
            for song in songs:
                yield Request(response.request.url + song, callback=self.parse_song)

    def parse_song(self, response):
        artist = response.xpath('//*[@class="col-xs-12 col-lg-8 text-center"]/*[@class="lyricsh"]/h2/b/text()').extract_first().replace("Lyrics", '')
        title = response.xpath('//*[@class="col-xs-12 col-lg-8 text-center"]/b/text()').extract_first().replace("\"", '')
        lyrics = ''.join(response.xpath('//*[@class="col-xs-12 col-lg-8 text-center"]/div/text()').extract()).strip()
        url = response.request.url

        if (not(lyrics and lyrics.strip) and not(title and title.strip) and not(artist and artist.strip)):
            return None
        else:
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


        
