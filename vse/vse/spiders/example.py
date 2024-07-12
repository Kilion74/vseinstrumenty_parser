import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["vseinstrumenti.ru"]
    start_urls = ["https://www.vseinstrumenti.ru/brand/lezard-13097/page3/#searchQuery=lezard&searchType=redirect"]

    def parse(self, response):
        heads = response.css('div.dGMJLz fSNq2j Ppy5qY LXySrk')
