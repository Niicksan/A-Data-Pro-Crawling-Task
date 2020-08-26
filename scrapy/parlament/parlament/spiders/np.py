# -*- coding: utf-8 -*-
import scrapy

class Parlament(scrapy.Spider):
    name = "parlament"
    start_urls = [
        'https://www.parliament.bg/bg/MP/2797',
        'https://www.parliament.bg/bg/MP/2678',
        'https://www.parliament.bg/bg/MP/2706',
        'https://www.parliament.bg/bg/MP/2716',
        'https://www.parliament.bg/bg/MP/2654',
        'https://www.parliament.bg/bg/MP/2651',
        'https://www.parliament.bg/bg/MP/2801',
        'https://www.parliament.bg/bg/MP/2712',
        'https://www.parliament.bg/bg/MP/2729',
        'https://www.parliament.bg/bg/MP/2672',
        'https://www.parliament.bg/bg/MP/2841',
        'https://www.parliament.bg/bg/MP/2874',
        'https://www.parliament.bg/bg/MP/2820',
        'https://www.parliament.bg/bg/MP/2666',
        'https://www.parliament.bg/bg/MP/2799',
        'https://www.parliament.bg/bg/MP/2866',
        'https://www.parliament.bg/bg/MP/2962',
        'https://www.parliament.bg/bg/MP/2753',
        'https://www.parliament.bg/bg/MP/2860',
        'https://www.parliament.bg/bg/MP/2666',
        'https://www.parliament.bg/bg/MP/2799',
        'https://www.parliament.bg/bg/MP/2929',
        'https://www.parliament.bg/bg/MP/2960',
        'https://www.parliament.bg/bg/MP/2700',
    ]

    def parse(self, response):
        for person in response.css('div.MPinfo'):
            yield {
                'day of birth': person.css('li:nth-child(1)::text').re(r'([\d{2}\/\d{2\/\d{4}])'),
                'profession': person.css('li::text').extract()[1],
                'languages': person.css('li::text').extract()[2],
                'Elected by political force': person.css('li::text').extract()[3],
                'Electoral district': person.css('li::text').extract()[4],
                'Email': person.css('div.MPinfo li:nth-child(7) a::text').get(),
            }
    

        # -*- -*- -*- -*- -*- -*- -*- -*- -*- -*-
        # next_page = response.css('div.MPinfo a::attr(href)').get()
        # if next_page is not None:
        #    next_page = response.urljoin(next_page)
        #    yield scrapy.Request(next_page, callback=self.parse)

        # next_urls = response.xpath('//div[@class="MPinfo"]//a/@href').extract()
        # for next_url in next_urls:
        #    yield Request(response.urljoin(next_url), callback=self.parse_anime_list_page)