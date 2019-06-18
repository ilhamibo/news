from rest_framework_elasticsearch.es_serializer import ElasticModelSerializer
from news.news.models import News
from news.news.documents import NewsIndex

class ElasticNewsSerializer(ElasticModelSerializer):
    class Meta:
        model = News
        es_model = NewsIndex
        fields = ('id', 'created',)
