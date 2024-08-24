import pymongo
import json
import os
from pymongo import MongoClient, InsertOne

client = pymongo.MongoClient('// write the connection string here')
db = client.newssite
collection = db.news
requesting = []

path_to_json = '/Users/vinaygosain/Desktop/Projects/news-please/newsplease/data/2024/08/23/timesofindia.indiatimes.com/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

for jsonFile in json_files:
    filePath = "%s%s" % (path_to_json, jsonFile)
    print ('filePath', filePath)
    with open(r"%s" % filePath) as f:
        for jsonObj in f:
            myDict = json.loads(jsonObj)
            requesting.append(InsertOne(myDict))

result = collection.bulk_write(requesting)
client.close()