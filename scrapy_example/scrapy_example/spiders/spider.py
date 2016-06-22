from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.item import Item, Field


class Website(Item):
    name = Field()
    description = Field()
    url = Field()

class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        hxs = Selector(response)

        sites = hxs.xpath('//ul[@class="directory-url"]/li')
        items = []

        for site in sites:
            item = Website()
            item['name'] = site.select('a/text()').extract()
            item['url'] = site.select('a/@href').extract()
            items.append(item)
        return items