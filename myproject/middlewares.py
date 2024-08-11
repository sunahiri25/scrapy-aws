# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import random


class MyprojectSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.
    def __init__(self, user_agents):
        self.user_agents = user_agents

    @classmethod
    def from_crawler(cls, crawler):
        user_agents = crawler.settings.get('USER_AGENTS', [])
        return cls(user_agents)

    def process_request(self, request, spider):
        user_agent = random.choice(self.user_agents)
        request.headers['User-Agent'] = user_agent



class MyprojectDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    def __init__(self, user_agents):
        self.user_agents = user_agents

    @classmethod
    def from_crawler(cls, crawler):
        user_agents = crawler.settings.get('USER_AGENTS', [])
        return cls(user_agents)

    def process_request(self, request, spider):
        user_agent = random.choice(self.user_agents)
        request.headers['User-Agent'] = user_agent

## middlewares.py

# from urllib.parse import urlencode
# from random import randint
# import requests

# class MyprojectSpiderMiddleware:

#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(crawler.settings)

#     def __init__(self, settings):
#         self.scrapeops_api_key = settings.get('SCRAPEOPS_API_KEY')
#         self.scrapeops_endpoint = settings.get('SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT', 'http://headers.scrapeops.io/v1/user-agents?') 
#         self.scrapeops_fake_user_agents_active = settings.get('SCRAPEOPS_FAKE_USER_AGENT_ENABLED', False)
#         self.scrapeops_num_results = settings.get('SCRAPEOPS_NUM_RESULTS')
#         self.headers_list = []
#         self._get_user_agents_list()
#         self._scrapeops_fake_user_agents_enabled()

#     def _get_user_agents_list(self):
#         payload = {'api_key': self.scrapeops_api_key}
#         if self.scrapeops_num_results is not None:
#             payload['num_results'] = self.scrapeops_num_results
#         response = requests.get(self.scrapeops_endpoint, params=urlencode(payload))
#         json_response = response.json()
#         self.user_agents_list = json_response.get('result', [])

#     def _get_random_user_agent(self):
#         random_index = randint(0, len(self.user_agents_list) - 1)
#         return self.user_agents_list[random_index]

#     def _scrapeops_fake_user_agents_enabled(self):
#         if self.scrapeops_api_key is None or self.scrapeops_api_key == '' or self.scrapeops_fake_user_agents_active == False:
#             self.scrapeops_fake_user_agents_active = False
#         self.scrapeops_fake_user_agents_active = True
    
#     def process_request(self, request, spider):        
#         random_user_agent = self._get_random_user_agent()
#         request.headers['User-Agent'] = random_user_agent
