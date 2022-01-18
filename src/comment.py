#%%
import requests
import json
import time

class Comments(object):
    def __init__(self, topic_id):
        self.url = "https://pantip.com/forum/topic/render_comments"
        self.topic_id = topic_id
        self.response_page_size = 100
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        }


    def get_comments(self, response, comments):
        data = json.dumps(response).replace("$", "")
        comment_list = json.loads(data)["comments"]
        comments.extend(comment_list)


    def extract_response(self, response, comments):
        if response["paging"]["max_comments"] > 0:
            self.get_comments(response=response, comments=comments)
            count = response["count"]
        else:
            count = 0

        return count


    def get_response(self, page):
        params = {
            "param": "page{}".format(page),
            "tid": self.topic_id,
        }

        response = requests.get(url=self.url, params=params, headers=self.headers)
        response = response.json()

        return response


    def process(self, counter):
        start_time = time.time()
        comments = []
        page = 1

        while True:
            response = self.get_response(page=page)
            count = self.extract_response(response=response, comments=comments)
            checker = count - ((page) * self.response_page_size)

            if checker <= 0:
                break
            
            page += 1

        exc_time = time.time() - start_time
        print("Comment Process -> Loop Round: {}, Topic Id: {}, Comment Lenght: {}, Time Execute: {}".format(counter, self.topic_id, len(comments), exc_time))

        return comments
# %%
