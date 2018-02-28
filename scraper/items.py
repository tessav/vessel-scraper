# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScheduleItem(scrapy.Item):
    arv_dt = scrapy.Field()
    vessel = scrapy.Field()
    cargo = scrapy.Field()
    qty = scrapy.Field()
    v_type = scrapy.Field()
    agent = scrapy.Field()


class PositionItem(scrapy.Item):
    berth = scrapy.Field()
    vessel = scrapy.Field()
    v_type = scrapy.Field()
    fc = scrapy.Field()
    berth_date = scrapy.Field()
    cargo = scrapy.Field()
    qty = scrapy.Field()
    day_handling = scrapy.Field()
    up_to_day_handling = scrapy.Field()
    balance = scrapy.Field()
    load_port = scrapy.Field()
    agent = scrapy.Field()


class MovementItem(scrapy.Item):
    move_date = scrapy.Field()
    vessel = scrapy.Field()
    status = scrapy.Field()
    berth_allotted = scrapy.Field()
    boarding_time = scrapy.Field()
