# import scrapy
# import json
# from . import globalVar as gl
# from . import githubCommitSpider
#
# #关键字
# searchWords = ["bug","fix"]
#
# class GithubSpider(scrapy.Spider):
#     name = "commitInfo"
#     allowed_domains = ["github.com"]
#     urls = []
#     with open("commit.json", 'r') as load_f:
#         load_dict = json.load(load_f)
#         urls = json.loads(load_dict)
#     # print(urls['url'])
#     start_urls = []
#     for url in urls['url']:
#         start_urls.append(url)
#
#     def parse(self, response):
#         commitDiv = response.css('#js-repo-pjax-container > div.container.new-discussion-timeline.experiment-repo-nav > div.repository-content > div.commit.full-commit.px-2.pt-2 > p::text').extract()
#         print(commitDiv[0])
#
#
