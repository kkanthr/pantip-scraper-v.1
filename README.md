# Pantip-Scraper
Pantip-Scraper is a scraping tool base on python that support to scrape topics from https://pantip.com by using website's API and extract data from HTML response.

## Workflow
![Workflow](https://user-images.githubusercontent.com/88326334/149983079-0981718a-eb7e-4dbe-a92f-5f5ebbf9f33d.png)

This project separate for 4 stages referenced by workflow of target website include store data into database.
- **Get search** : get topics from search keyword
- **Get mainpost** : get mainpost data of topic
- **Get comments** : get comments data of topic
- **Insert to DB** : insert data is **RAW DATA**

## Limitation
Speed of the tool is ~2.5-3 seconds per topic.
The problem of this version is **Get mainpost**, because it's only one part that have to load HTML response and extract data.

## Requirements
- pymongo
- python-dotenv
- requests
- beautifulsoup4

**In project have docker-compose for create mongoDB. But if you have your own database(mongoDB), you can change config in .env by yourself.**
