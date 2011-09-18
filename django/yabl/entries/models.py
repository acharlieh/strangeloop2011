import datetime
from django.db import models
from yabl.authors.models import Author

# Create your models here.
class Entry(models.Model):
    author = models.ForeignKey(Author, related_name='entries')
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    is_published = models.BooleanField(default=True)
    headline = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.TextField()
    body = models.TextField()

    def __unicode__(self): 
        return self.headline
