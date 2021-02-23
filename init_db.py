import requests
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

# 고양이 사진 DB에 추가
for i in range(55):
    res = requests.get('https://api.thecatapi.com/v1/images/search')
    id = i + 1
    url = res.json()[0]['url']
    print(f'{id} : {url}')
    db.cat.insert_one({'id': id, 'url': url})
