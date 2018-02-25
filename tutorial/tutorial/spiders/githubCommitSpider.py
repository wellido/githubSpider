import scrapy
import json
from . import globalVar as gl
# from tutorial.items import commitItem
#搜索数目
global searchNum
searchNum = 50
#第一次Older标签
global olderPage
olderPage = 1

gl._init()
class GithubSpider(scrapy.Spider):
    name = "githubCommit"
    allowed_domains = ["github.com"]
    url = 'https://github.com/tensorflow/tensorflow/commits/master/'
    start_urls = [url]

    def parse(self, response):
        # item = commitItem()
        commitDict = {}
        for olIndex in range(1,11):
            if response.xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[2]/ol[' + str(olIndex) + ']'):
                for liIndex in range (1,101):
                    li = response.xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[2]/ol[' + str(olIndex) + ']/li[' + str(liIndex) + ']')
                    if li:
                        for divIndex in range (1,3):
                            href = response.xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[2]/ol[' + str(olIndex) + ']/li[' + str(liIndex) + ']/div[2]/div[' + str(divIndex) + ']/a/@href').extract()
                            if href:
                                global searchNum
                                if searchNum >= 0:
                                    searchNum = searchNum - 1
                                    gl.set_GlobalVar('https://github.com' + href[0])
                                    # item['commitUrl'] = 'https://github.com' + href[0]
                                    # yield item
                                else:
                                    commitDict['url'] = gl.urlList
                                    json_str = json.dumps(commitDict)
                                    with open("commit.json", "w") as f:
                                        json.dump(json_str, f)
                                        print("加载入文件完成...")
                                    return 0
                            else: break
                    else:
                        break
            else: break
        global olderPage
        if olderPage >= 1:
            nextPage = response.xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[3]/div/a/@href').extract()
            olderPage = olderPage - 1
            yield response.follow(nextPage[0], self.parse)
        else:
            nextPage = response.xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[3]/div/a[2]/@href').extract()
            yield response.follow(nextPage[0], self.parse)






