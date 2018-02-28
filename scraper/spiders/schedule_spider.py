import scrapy
from scraper.items import ScheduleItem
from datetime import datetime as dt

SCHEDULE_TABLE_ORDER = 2
STARTING_ROW_ID = 2

class ScheduleSpider(scrapy.Spider):
    name = "schedule"

    def start_requests(self):
        urls = [
            'http://cochinport.gov.in/index.php?opt=shipsatport&cat=ev&tab=0'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        schedule_list = response.css('table.shipsinport')[SCHEDULE_TABLE_ORDER].css('tr')[STARTING_ROW_ID:]
        for schedule in schedule_list:
            row = schedule.css('td')
            vs = ScheduleItem()
            s_date = row[0].css('::text').extract_first()
            s_time = row[1].css('::text').extract_first()
            vs['arv_dt'] = dt.strptime('{} {}'.format(s_date, s_time), '%d.%m.%Y %H:%M')
            vs['vessel'] = row[2].css('::text').extract_first()
            vs['cargo'] = row[3].css('::text').extract_first()
            vs['qty'] = row[4].css('::text').extract_first()
            vs['v_type'] = row[5].css('::text').extract_first()
            vs['agent'] = row[6].css('::text').extract_first()
            self.logger.info(vs)
            yield vs
