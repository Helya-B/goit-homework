from django.core.management.base import BaseCommand
import logging

import scrapy
from itemadapter import ItemAdapter
from scrapy.crawler import CrawlerProcess
from scrapy.item import Item, Field

from ...models import Quote, Author

class Command(BaseCommand):
    def handle(self, **options):
        logging.getLogger('scrapy').propagate = False

        process = CrawlerProcess()
        process.crawl(QuotesSpider)
        process.start()


class QuoteItem(Item):
    quote = Field()
    author = Field()
    tags = Field()

class AuthorItem(Item):
    fullname = Field()
    born_date = Field()
    born_location = Field()
    description = Field()

class DataPipline:
    quotes = []
    authors = []

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if "fullname" in adapter.keys():
            self.authors.append(dict(adapter))
        if "quote" in adapter.keys():
            self.quotes.append(dict(adapter))

    def close_spider(self, spider):
        for author in self.authors:
            existing_author = Author.objects.filter(fullname=author.get("fullname")).first()
            if existing_author:
                continue

            new_author = Author(
                fullname=author.get("fullname"),
                born_date=author.get("born_date"),
                born_location=author.get("born_location"),
                description=author.get("description"),
            )
            new_author.save()
        for quote in self.quotes:
            author = Author.objects.filter(fullname=quote.get("author")).first()
            new_quote = Quote(quote=quote.get("quote"), tags=quote.get("tags"), author=author)
            new_quote.save()

class QuotesSpider(scrapy.Spider):
    name = "get_quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]
    custom_settings = {"ITEM_PIPELINES": {DataPipline: 300}}

    def parse(self, response, **kwargs):
        for q in response.xpath("/html//div[@class='quote']"):
            quote = q.xpath("span[@class='text']/text()").get().strip()
            author = q.xpath("span/small[@class='author']/text()").get().strip()
            tags = q.xpath("div[@class='tags']/a/text()").extract()
            yield QuoteItem(quote=quote, author=author, tags=tags)
            yield response.follow(
                url=self.start_urls[0] + q.xpath("span/a/@href").get(),
                callback=self.parse_author,
            )

        next_link = response.xpath("/html//li[@class='next']/a/@href").get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link)

    @classmethod
    def parse_author(cls, response, **kwargs):
        content = response.xpath("/html//div[@class='author-details']")
        fullname = content.xpath("h3[@class='author-title']/text()").get().strip()
        fullname = fullname.replace("-", " ")

        born_date = (
            content.xpath("p/span[@class='author-born-date']/text()").get().strip()
        )
        born_location = (
            content.xpath("p/span[@class='author-born-location']/text()").get().strip()
        )
        description = (
            content.xpath("div[@class='author-description']/text()").get().strip()
        )

        yield AuthorItem(
            fullname=fullname,
            born_date=born_date,
            born_location=born_location,
            description=description,
        )
