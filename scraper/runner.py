from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from scraper.spiders.schedule_spider import ScheduleSpider
from scraper.spiders.position_spider import PositionSpider
from scraper.spiders.movement_spider import MovementSpider

configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})


def run_spiders():
    runner = CrawlerRunner(get_project_settings())

    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(ScheduleSpider)
        yield runner.crawl(PositionSpider)
        yield runner.crawl(MovementSpider)
        reactor.stop()

    crawl()
    reactor.run()
