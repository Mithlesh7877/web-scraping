import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        all_data=response.xpath('//tbody/tr')
        for i in all_data:
            count = i.xpath('.//td[1]/a/text()').get()
            gdp=i.xpath('.//td[2]/text()').get()
            yield{
                'country':count,
                'gdp':gdp
            }