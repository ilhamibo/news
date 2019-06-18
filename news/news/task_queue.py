from celery import shared_task

from news.news.models import News


@shared_task
def queue_create_news(data):
    news = News.objects.create(**data)
    return f'id news {news.id} created with success!'
