import scrapy
from tutorial.items import TutorialItem
#搜索开始索引
searchStart = 20
#搜索数目
searchNum = 20
#关键字
searchWords = ["bug","fix"]
#第一次Older标签
global olderPage
olderPage = 1

class GithubSpider(scrapy.Spider):
    name = "githubCommit"
    allowed_domains = ["github.com"]
    url = 'https://github.com/tensorflow/tensorflow/commits/master/'
    start_urls = [url]

    def parse(self, response):
        for olIndex in range(1,11):
            if response.xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[2]/ol[' + str(olIndex) + ']'):
                print("ololol",olIndex)
                for liIndex in range (1,101):
                    li = response.xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[2]/ol[' + str(olIndex) + ']/li[' + str(liIndex) + ']')
                    if li:
                        print("lilili",liIndex)
                        for divIndex in range (1,3):
                            href = response.xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[2]/ol[' + str(olIndex) + ']/li[' + str(liIndex) + ']/div[2]/div[' + str(divIndex) + ']/a/@href').extract()
                            if href:
                                print("divdiv", divIndex)
                                print(href)
                            else: break
                    else:
                        print("No!!!",liIndex)
                        break
            else: break
        global olderPage
        if olderPage >= 1:
            nextPage = response.xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[3]/div/a/@href').extract()
            olderPage = olderPage - 1
            print(nextPage[0])
            yield response.follow(nextPage[0], self.parse)
        else:
            nextPage = response.xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[3]/div/a[2]/@href').extract()
            print(nextPage[0])
            yield response.follow(nextPage[0], self.parse)








