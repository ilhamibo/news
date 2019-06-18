from django.contrib import admin
from news.news.models import News

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'body',)
    search_fields = ('author',)

admin.site.register(News, NewsAdmin)
