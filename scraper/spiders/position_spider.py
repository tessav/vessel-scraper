import scrapy
from scraper.items import PositionItem
from datetime import datetime as dt
import scraper.utils as utils

POSITION_TABLE_ORDER = 0
STARTING_ROW_ID = 2

class PositionSpider(scrapy.Spider):
    name = "position"

    def start_requests(self):
        urls = [
            'http://cochinport.gov.in/index.php?opt=shipsatport&cat=ev&tab=0'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        position_list = response.css('table.shipsinport')[POSITION_TABLE_ORDER].css('tr')[STARTING_ROW_ID:]
        for position in position_list:
            row = position.css('td')
            vp = PositionItem()
            vp['berth'] = row[0].css('label::text').extract_first()
            vp['vessel'] = utils.parse_vessel_name(row[1].css('label::text').extract_first())
            vp['v_type'] = row[2].css('label::text').extract_first()
            vp['fc'] = row[3].css('label::text').extract_first()
            berth_date = row[4].css('label::text').extract_first()
            vp['berth_date'] = dt.strptime(berth_date, '%d.%m.%Y') if berth_date else None
            vp['cargo'] = row[5].css('label::text').extract_first()
            vp['qty'] = row[6].css('label::text').extract_first()
            vp['day_handling'] = row[7].css('label::text').extract_first()
            vp['up_to_day_handling'] = row[8].css('label::text').extract_first()
            vp['balance'] = row[9].css('label::text').extract_first()
            vp['load_port'] = row[10].css('label::text').extract_first()
            vp['agent'] = row[11].css('::text').extract_first()
            yield vp
