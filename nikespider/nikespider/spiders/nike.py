import json
from typing import Iterable, Any

import scrapy
from scrapy import cmdline
from starlette.responses import JSONResponse, HTMLResponse
import re
from loguru import logger

class NikeSpider(scrapy.Spider):
    name = "nike"
    allowed_domains = ["www.nike.com.cn"]

    def start_requests(self):
        url = "https://api.nike.com.cn/cic/browse/v2?queryid=products&anonymousId=DSWX82E53418DF4F4624DA18EB7B1CCEC5E0&country=cn&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(CN)%26filter%3Dlanguage(zh-Hans)%26filter%3DemployeePrice(true)%26anchor%3D{}%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=zh-Hans&localizedRangeStr=%7BlowestPrice%7D%20%E2%80%94%20%7BhighestPrice%7D"
        for i in range(2):
            yield scrapy.Request(url.format(i*24), dont_filter=True, callback=self.parse)


    def parse(self, response: JSONResponse):
        baseUrl = 'https://www.nike.com.cn'
        res = json.loads(response.body.decode())
        ls = res['data']['products']['products']
        detailLinks = [l.get('url').replace('{countryLang}', baseUrl) for l in ls]
        for link in detailLinks:
            yield scrapy.Request(link, callback=self.detail_parse)



    def detail_parse(self, response: HTMLResponse):
        res = response.body.decode()
        pattern = '<script id="__NEXT_DATA__" type="application/json">\s*({.*?})\s*</script>'
        jsonData = re.search(pattern, res)
        jsonData = json.loads(jsonData.group(1))
        sku = jsonData["query"].get("styleColor")
        data = jsonData["props"]["pageProps"]["productGroups"][0]["products"][sku]
        item = {
            "title": data["productInfo"].get("title"),
            "price": data["prices"],
            "color": data["colorDescription"],
            "size": data["sizes"],
            "sku": data["styleCode"],
            "detailes": data["productInfo"],
            "imageUrls": [
                item["properties"]["squarish"]["url"].replace('t_default', 't_PDP_1728_v1/f_auto,q_auto:eco') for
                item in data["contentImages"]]
        }
        yield item



if __name__ == '__main__':
    cmdline.execute('scrapy crawl nike'.split())
