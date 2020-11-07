from django.db import models

# Create your models here.
class ShortUrl(models.Model):
    url = models.URLField(blank = False)
    shorturl = models.CharField(blank = False, max_length = 8)
    visits = models.IntegerField(default = 0)
