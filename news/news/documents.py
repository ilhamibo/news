from elasticsearch_dsl import Document, Integer, Date
from elasticsearch import Elasticsearch, RequestsHttpConnection
from elasticsearch_dsl.connections import connections


connections.create_connection(hosts=['localhost:9200/'])

class NewsIndex(Document):
    id = Integer()
    created = Date()

    class Index:
        name = 'news'
