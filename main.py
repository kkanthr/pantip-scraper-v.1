from src.comment import Comments
from src.getsearch import GetSearch
from src.mainpost import MainPost

from database import MongoDB


search_key = "{add your search key in here}"
counter = 1

collection = MongoDB().connect()

get_search = GetSearch(search_key=search_key)
total_page = get_search.get_total_page()

for const in range(total_page):
    page = const + 1
    topic_ids = get_search.process(page=page)
    
    for topic_id in topic_ids:
        result = {}

        main_post = MainPost(topic_id=topic_id)
        comments = Comments(topic_id=topic_id)

        main_post_data = main_post.process(counter=counter)
        comments_data = comments.process(counter=counter)

        result["mainpost"] = main_post_data
        result["comments"] = comments_data
        result["topic_id"] = topic_id
        result["search_key"] = search_key

        collection.insert_one(result)

        counter += 1