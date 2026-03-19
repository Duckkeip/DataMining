import scrapy
from scrapy.crawler import CrawlerProcess

class Spider(scrapy.Spider):
    name = "test"

    def start_requests(self):
        yield scrapy.Request("https://quotes.toscrape.com", self.parse)

    def parse(self, response):
        for q in response.css("div"):
            print(q.css(".text::text").get())
            print(q.css(".author::text").get())
            print("------")

process = CrawlerProcess()
process.crawl(Spider)
process.start()