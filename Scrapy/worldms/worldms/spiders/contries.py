import scrapy
import logging

class ContriesSpider(scrapy.Spider):
    name = 'contries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries=response.xpath('//td/a')
        for cn in countries:
            name = cn.xpath('.//text()').get()
            link = cn.xpath('.//@href').get()
            # not worked so used urljoin abs_url=f'https://www.worldometers.info{link}'
            # abs_url=response.urljoin(link)
            yield response.follow(url=link,callback=self.parse_country,meta={'country_name':name})#send request to each website from main page and to save response created another parse countries
            #yeilded output for url yield scrapy.Request(url=abs_url)
            # yield{
            # 'title':name,
            # 'countries':link
            #      }

    def parse_country(self,response):
        name =response.request.meta['country_name']
        rows=response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
        for r in rows:
            year=r.xpath('.//td[1]/text()').get()
            population= r.xpath('.//td[2]/strong/text()').get()

            yield{
                'country_name':name,
                'year':year,
                'popn':population
            }