#encoding=utf-8 
from scrapy import Spider
from scrapy.selector import Selector
from image_spider.items import ImageItem

class dbmeiziSpider(Spider):
	name = "images_spider"
	allowed_domin =["doubanmeizi.com"]
	start_urls = [
		"http://www.doubanmeizi.com",
		"http://www.doubanmeizi.com/page/2/",
		"http://www.doubanmeizi.com/page/3/",
		"http://www.doubanmeizi.com/page/4/",
		"http://www.doubanmeizi.com/page/5/",
		"http://www.doubanmeizi.com/page/6/",
		"http://www.doubanmeizi.com/page/7/",
		"http://www.doubanmeizi.com/page/8/",
		"http://www.doubanmeizi.com/page/9/",
		"http://www.doubanmeizi.com/page/10/",
		"http://www.doubanmeizi.com/page/11/",
		"http://www.doubanmeizi.com/page/12/",
		"http://www.doubanmeizi.com/page/13/",
		"http://www.doubanmeizi.com/page/14/",
		"http://www.doubanmeizi.com/page/15/",
		"http://www.doubanmeizi.com/page/16/",
	]
	def parse(self, response):
		postlist = Selector(response).xpath('//div[@class="postlist"]')
		images = []
		for list in postlist:
			array = list.xpath('div/div/h2/a/text()').extract()
			if len(array) > 0:
				title = array[0]
			else:
				title = ''
			array1 = list.xpath('div/div/h2/a/@href').extract()
			if len(array1) > 0:
				titleurl = array1[0]
			else:
				titleurl = ''

			array = list.xpath('div/div[@class="metaLeft"]/div[@class="day"]/text()').extract()
			if len(array) > 0:
				updateday = array[0]
			else:
				updateday = ''

			array = list.xpath('div/div[@class="metaLeft"]/div[@class="month_Year"]/text()').extract()
			if len(array) > 0:
				updatedate = array[0]
			else:
				updatedate = ''

			array = list.xpath('div[@class="postContent"]/div/p/img/@alt').extract()
			if len(array) > 0:
				dataid = array[0]
			else:
				dataid = ''

			array = list.xpath('div[@class="postContent"]/div/p/img/@width').extract()
			if len(array) > 0:
				width = array[0]
			else:
				width = 0

			array = list.xpath('div[@class="postContent"]/div/p/img/@height').extract()
			if len(array) > 0:
				height = array[0]
			else:
				height = 0

			array = list.xpath('div[@class="postContent"]/div/p/text()').extract()
			if len(array) > 0:
				desc = array[0]
			else:
				desc = ''

			array = list.xpath('div[@class="postContent"]/div/p/img/@src').extract()
			if len(array) > 0:
				imageurl = array[0]
			else:
				imageurl = ''
			images.append(imageurl)
		item = ImageItem()
		item['image_urls']=images
		return item