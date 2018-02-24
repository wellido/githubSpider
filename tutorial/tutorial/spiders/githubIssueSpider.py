import scrapy
from tutorial.items import TutorialItem
#搜索开始索引
searchStart = 20
#搜索数目
searchNum = 20
#关键字
searchWords = ["bug","fix"]

class GithubSpider(scrapy.Spider):
    name = "githubIssue"
    allowed_domains = ["github.com"]
    url = 'https://github.com/tensorflow/tensorflow/issues/'
    start_urls = []
    for pageNum in range(searchStart, searchStart + searchNum):
        start_urls.append(url + '/' + str(pageNum))

    def parse(self, response):
        item = TutorialItem()
        title = response.selector.css('#partial-discussion-header > div.gh-header-show > h1 > span.js-issue-title::text').extract()
        for keyWord in searchWords:
            if keyWord in title[0]:
                print(title[0])
            else:
                print("Not this one")
        # item['title'] = response.selector.css('#partial-discussion-header > div.gh-header-show > h1 > span.js-issue-title::text').extract()

