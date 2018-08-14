from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    image_url = models.CharField(max_length=200, null=True, blank=True)
    vote = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-vote',)

    def __str__(self):
        return self.title