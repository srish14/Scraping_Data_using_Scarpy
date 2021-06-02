import scrapy
from ..items import QuotetutorialItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):

        items = QuotetutorialItem()

        # title = response.css('title::text').extract()
        # yield ('titletext' : title)

        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items

            # {
            #     'title' : title,
            #     'author' : author,
            #     'tag' : tag
            # }

