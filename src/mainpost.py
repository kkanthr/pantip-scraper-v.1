from bs4 import BeautifulSoup
import requests
import re
import time

class MainPost(object):
    def __init__(self, topic_id):
        self.topic_id = topic_id
        self.url = "https://pantip.com/topic/{}".format(self.topic_id)
        self.regex_like_score = re.compile('^like-score')
        self.regex_emotion_score = re.compile('^emotion-score')


    def get_post(self, soup):
        post_div = soup.find(id="topic-{}".format(self.topic_id))

        return post_div


    def get_post_title(self, post_div, data):
        data["title"] = post_div.find(class_="display-post-title").text

        return data
    

    def get_post_content(self, post_div, data):
        post_content_div = post_div.find(class_="display-post-story")
        data["text"] = post_content_div.text
        data["img_url"] = [ i["src"] for i in post_content_div.find_all("img") ]

        return data


    def get_post_tag(self, post_div, data):
        tag_div = post_div.find(class_="display-post-tag-wrapper")
        data["tag"] = [ i.attrs for i in tag_div.find_all('a')]

        return data


    def get_like_score(self, post_div, data):
        like_score_div = post_div.find(class_=self.regex_like_score)
        data["like_score"] = int(like_score_div.text)

        return data


    def get_emotion_score(self, post_div, data):
        emotion_score_list = post_div.find(class_="emotion-vote-choice small-txt-fixed").find_all('span', class_="emotion-choice-score")[1:]

        data["emotion"] = {}
        data["emotion"]["sum"] = int(post_div.find(class_=self.regex_emotion_score).text)
        data["emotion"]["like"] = int(emotion_score_list[0].text)
        data["emotion"]["laugh"] = int(emotion_score_list[1].text)
        data["emotion"]["love"] = int(emotion_score_list[2].text)
        data["emotion"]["impress"] = int(emotion_score_list[3].text)
        data["emotion"]["scary"] = int(emotion_score_list[4].text)
        data["emotion"]["wow"] = int(emotion_score_list[5].text)

        return data


    def extract_data(self, soup, data):
        post_div = self.get_post(soup=soup)

        data = self.get_post_title(post_div=post_div, data=data)
        data = self.get_post_content(post_div=post_div, data=data)
        data = self.get_post_tag(post_div=post_div, data=data)
        data = self.get_like_score(post_div=post_div, data=data)
        data = self.get_emotion_score(post_div=post_div, data=data)

        return data


    def response_to_soup(self, response):
        soup = BeautifulSoup(response.content, 'html.parser')

        return soup


    def process(self, counter):
        start_time = time.time()
        data = {}

        response = requests.get(self.url)
        soup = self.response_to_soup(response=response)
        data = self.extract_data(soup=soup, data=data)

        exc_time = time.time() - start_time
        print("MainPost Process -> Loop Round: {}, Topic Id: {}, Time Execute: {}".format(counter, self.topic_id, exc_time))

        return data
