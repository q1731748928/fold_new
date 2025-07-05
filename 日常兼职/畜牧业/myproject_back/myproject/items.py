import scrapy

class GleamiItem(scrapy.Item):
    # define the fields for your item here like:
    region = scrapy.Field()
    country = scrapy.Field()
    animal_species = scrapy.Field()
    herd = scrapy.Field()
    feed = scrapy.Field()
    manure = scrapy.Field()
