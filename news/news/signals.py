from django.db.models.signals import post_save
from django.dispatch import receiver

from news.news.models import News

from .serializers import ElasticNewsSerializer


@receiver(post_save, sender=News, dispatch_uid="save_record")
def index_post(sender, instance, **kwargs):
    obj = ElasticNewsSerializer(instance)
    obj.save()
