from django.test import TestCase
from django.test.client import Client

from elasticsearch import Elasticsearch
from elasticsearch_dsl.connections import connections

from news.news.documents import NewsIndex
from news.news.models import News

import json


class ApiViewTest(TestCase):

    def setUp(self):
        connections.create_connection(hosts=['localhost:9200/'])
        self.es = Elasticsearch() 
        NewsIndex.init()
        self.headers = {'content_type': 'application/json'}
        self.client = Client()

    def test_news(self):
        News.objects.all().delete()
        self.es.indices.delete(index='news', ignore=[400, 404])

        data = {
            "id": 1,
            "author": "ilham syaiful akbar",
            "body": "New Journey Amiin"
        }
        
        headers = {'content_type': 'application/json'}
        response = self.client.post(reverse('news_create'), json.dumps(data), **self.headers)

        news_count = News.objects.all().count()
        self.assertEqual(response.status_code, 200)
        # checking in DB
        self.assertEqual(news_count, 1)

        # checking in Elasticsearch
        self.assertEqual(self.es.get(index='news', id=1, doc_type='doc')['_source']['id'], 1)

        response = self.client.post(reverse('news_create'), json.dumps(data), **self.headers)
        self.assertEqual(response.status_code, 400)

    def test_get_news(self):
        response = self.client.get(reverse('news'), **self.headers)
        response_json = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_json['count']), 1)
