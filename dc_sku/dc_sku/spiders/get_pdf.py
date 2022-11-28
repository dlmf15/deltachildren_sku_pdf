import scrapy
import pandas as pd

class GetPdfSpider(scrapy.Spider):
    name = 'get_pdf'

    def start_requests(self):
        df = pd.read_csv("/Users/devalou/PycharmProjects/deltachildren_sku_pdf/dc_sku/dc_sku/sku_urls_01092021.csv")
        urls = df['urls'].tolist()
        urls = list(dict.fromkeys(urls))
        urls.remove('not found')
        print(urls)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield{
            'url': response.request.url,
            'sku': response.xpath('//*[@id="display_sku"]/text()').get(),
            'pdf': response.xpath('//div[@id="product-assembly"]//a/@href').get()
        }

