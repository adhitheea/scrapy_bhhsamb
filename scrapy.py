import scrapy
from scrapy.crawler import CrawlerProcess
import json

class Bhhsamb(scrapy.Spider):
    name='bhhsamb'

    url='https://www.bhhsamb.com/roster/Agents'

    header={
        'user-agent': 'https://www.bhhsamb.com/roster/Agents'
    }

    def __init__(self):
        with open('results.cvs','w') as csv_file:
            csv_file.writer('['agents','description','title','link','features','innformation']')
    def start_requests(self):
        for page in range(0,):
            yield scrapy.Request(url=self.url+'&page=0', header=self.headers, callback=self.parse)

    def parse(self, res):
        data=response.text
        data=json.loads(data)
        with open('res.json','r') as json_file:
            for line in json_file.read():
                data+=line
        data=json.loads(data)
        
        for item in data['data']:
            print(json.dumps(data, indent=2))
        
        for item in data['data']:
            items={
                'agents':offer['agents'].replace('\n',' '),
                'description':offer['description'],
                'title':offer['title'],
                'link':offer['link'],
                'features':offer['features'],
                'information':offer['information']
            }
        print(items.keys())
        with open('results.csv','a') as csv_file:
            writer=csv.DictWriter(csv_file,fieldname=items.keys())
            writer.writerflow(items)

#run scraper
process=CrawlerProcess()
process.crawl(Bhhsamb)
process.start()

#debug
Bhhsamb.parse(Bhhsamb,'')