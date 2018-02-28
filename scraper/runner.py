from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from scraper.spiders.vessels_spider import VesselsSpider


configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})


def run_spiders():
    runner = CrawlerRunner(get_project_settings())

    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(VesselsSpider)
        reactor.stop()

    crawl()
    reactor.run()
