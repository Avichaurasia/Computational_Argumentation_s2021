import scrapy
from selenium import webdriver

class CrawlQuotesSpider(scrapy.Spider):

	#assignment=[]

	name = "debate_crawler"
	allowed_domains = ["debate.org"]
	def start_requests(self):
		#predefinded pages to crawl
		url = 'https://www.debate.org/opinions/?sort=popular'

		#for url in urls:
		request = scrapy.Request(url=url, callback=self.parse_tag)
		yield request

	def parse_tag(self, response):



		df=response.css('#opinions-list li')
		#print("vai-------->",df)
		df.pop(1)
		for tags in df[0:5]:
			#print("avi")
			g=tags.css('a ::attr(href)').get()
			new_url="https://www.debate.org"+g
			print('URL is============================>',new_url)
			#print(u)
			request = scrapy.Request(url=new_url, callback=self.parse_urls)
			#print(request)
			yield request
			#print()




	def parse_urls(self, resposne):

		#df1 = response.css('#breadcrumb a')

		#load_arguments=resposne.css('.debate-more-btn').onclick()
		#print("Avinash-------------->",load_arguments)

		#options = webdriver.ChromeOptions()
		#options.binary_location = "/Applications/Google Chrome.app/contents/MacOS/Google Chrome"
		#chrome_driver_binary = "/usr/local/bin/chromedriver"
		#browser = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
		#browser.get("https://www.debate.org/opinions/do-you-agree-with-the-black-lives-matter-movement-1")
		#elem = browser.find_element_by_xpath('//a[class="debate-more-btn"]')
		#elem.click()
		#time.sleep(0.2)
		#elem = browser.find_element_by_xpath("//#debate #yes-arguments li")
		#print('Avinash--------------->',elem)

		#elem.get_attribute("outerHTML")






		category=resposne.css('#breadcrumb a::text')[2].get()
		print('Category is--------->', category)
		topic_page = resposne.css('.debate-content .r-contain span ::text').get()
		print("Topic is===============>", topic_page)
		#print("avinash===============>", df1)
		Yes_tag_list = resposne.css('#debate #yes-arguments li')
		#header=""
		title=[]
		#bod=""
		body=[]
		for tags in Yes_tag_list:
			header=tags.css('h2 ::text').get()
			title.append(header)
			bod=tags.css('p ::text').getall()
			bod="".join(x for x in bod)

			#bod=" ".join(i for i in bod)

			body.append(bod)
			#print("Tile is======>", header, " ", 'Body is====================>', body)

		#for i,j in zip(title,body):
		#	print("Tile is======>", i, " ", 'Body is====================>', j)
		#	print()





		Pro_arguments={}
		for key,value in zip(title,body):
			Pro_arguments[key]=value

		Pro_arguments_copy=Pro_arguments.copy()

		Pro_arguments_updated=[]
		Pro_arguments_updated.append(Pro_arguments_copy)

		#print(Pro_arguments_updated)


		#print()
		#print()


		#print("===============>",pro_arguments)

		No_tag_list = resposne.css('#debate #no-arguments li')
		#No_header = ""
		No_title = []
		#No_bod = ""
		No_body = []
		for No_tags in No_tag_list:
			No_header = No_tags.css('h2 ::text').get()
			No_title.append(No_header)
			No_bod = No_tags.css('p ::text').extract()
			No_bod="".join((x for x in No_bod))
			No_body.append(No_bod)

		#print("No Argument header==================>",No_title)
		#print("No Argument body=====================>",No_body)

		Con_arguments = {}
		for key, value in zip(No_title, No_body):
			Con_arguments[key] = value

		Con_arguments_copy=Con_arguments.copy()
		Con_arguments_updated=[]
		Con_arguments_updated.append(Con_arguments_copy)

		#print(Con_arguments_updated)



		diction={}
		diction['topic']=topic_page
		diction['category']=category



		diction['pro_arguments']=Pro_arguments_updated
		diction['con_arguments']=Con_arguments_updated




		#print(diction)
	#	assignment.append(diction)


		yield diction























