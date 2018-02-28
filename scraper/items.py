# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class VesselItem(scrapy.Item):
    arv_dt = scrapy.Field()
    vessel = scrapy.Field()
    cargo = scrapy.Field()
    qty = scrapy.Field()
    v_type = scrapy.Field()
    agent = scrapy.Field()
