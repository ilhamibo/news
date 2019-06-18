from django.db import models


class News(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return f"{self.id}-{self.author}"
