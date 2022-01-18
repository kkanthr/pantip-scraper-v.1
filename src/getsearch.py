#%%
import requests
import math
import json

class GetSearch(object):
    def __init__(self, search_key):
        self.url = "https://pantip.com/search/search/get_search"
        self.timeout = 2
        self.page_limit = 1000
        self.response_page_size = 10
        self.search_key = search_key
        self.headers = {
            "x-requested-with": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
        }


    def fetch(self, payload):
        while True:
            try:
                response = requests.post(url=self.url, headers=self.headers, data=payload, timeout=self.timeout)
                break
            except:
                continue

        return response


    def get_data(self, response):
        res = response.json()
        res = res["response"]
        res = json.loads(res)

        return res


    def get_total_page(self):
        payload = {
            "inputtext": self.search_key,
            "page": 1
        }
        response = self.fetch(payload=payload)
        data = self.get_data(response=response)
        total_post = data["total"]
        total_page = math.ceil(total_post / self.response_page_size)
        
        if total_page > self.page_limit:
            total_page = self.page_limit
        
        return total_page


    def process(self, page):
        payload = {
            "inputtext": self.search_key,
            "page": page
        }
        response = self.fetch(payload=payload)
        data = self.get_data(response=response)
        topic_ids = [ item["topic_id"] for item in data["data"] ]

        return topic_ids