from elasticsearch import Elasticsearch, RequestsHttpConnection

from rest_framework_elasticsearch import es_views, es_pagination, es_filters
from rest_framework.decorators import list_route
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from news.news.documents import NewsIndex
from news.news.models import News
from news.news.task_queue import queue_create_news


class ListNewsView(es_views.ListElasticAPIView):
    es_client = Elasticsearch(hosts=['localhost:9200/'],
                              connection_class=RequestsHttpConnection)
    es_model = NewsIndex
    es_ordering_fields = (
        "created",
    )


class NewsCreateView(APIView):

    def post(self, request):
        news_id = request.data['id']
        response = {"message": "successfully creating news", "status_code": status.HTTP_200_OK}
        if News.objects.filter(id=news_id).exists():
            response.update(
                {
                    "message":f"Cannot create news, Id {news_id} already exists.",
                    "status_code": status.HTTP_400_BAD_REQUEST
                }
            )
            return Response(response, status=status.HTTP_400_BAD_REQUEST)    
        queue_create_news.delay(request.data)
        
        return Response(response, status=status.HTTP_200_OK)
