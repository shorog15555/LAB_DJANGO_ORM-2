from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=2048)
    description = models.TextField()
    rating = models.FloatField()
    is_published = models.BooleanField(default=True)
    release_date = models.DateField()



