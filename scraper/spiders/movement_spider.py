import scrapy
from scraper.items import MovementItem
from datetime import datetime as dt
import scraper.utils as utils

MOVEMENT_TABLE_ORDER = 1
STARTING_ROW_ID = 2
DATE_CLASS = 'hed1'
STATUS_CLASS = 'hed'

class MovementSpider(scrapy.Spider):
    name = "movement"

    def __init__(self):
        self.current_status = None
        self.current_date = None

    def start_requests(self):
        urls = [
            'http://cochinport.gov.in/index.php?opt=shipsatport&cat=ev&tab=0'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        movement_list = response.css('table.shipsinport')[MOVEMENT_TABLE_ORDER].css('tr')[STARTING_ROW_ID:]
        for movement in movement_list:
            class_list = movement.xpath('td/@class').extract()
            if not class_list: # row does not contain status or date, contains row data
                vm = self.extract_row(movement, 1)
                yield vm
            elif class_list[0] == 'hed1': # row contains move date
                self.current_date = movement.css('td::text').extract()[0]
            elif class_list[0] == 'hed': # row contains status & row data
                self.current_status = movement.css('td::text').extract()[0]
                vm = self.extract_row(movement, 0)
                yield vm

    def extract_row(self, movement, start_col):
        # start_col is the column of td with label to start extracting data
        row = movement.css('td label')
        vm = MovementItem()
        vm['move_date'] = dt.strptime(self.current_date, '%d/%m/%Y')
        vm['status'] = self.current_status
        vm['vessel'] = utils.parse_vessel_name(row[start_col].css('::text').extract_first())
        vm['berth_allotted'] = row[start_col + 1].css('::text').extract_first()
        boarding_time = row[start_col + 2].css('::text').extract_first()
        vm['boarding_time'] = dt.strptime(boarding_time, '%H:%M').time() if boarding_time else None
        return vm
