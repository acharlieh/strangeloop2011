from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

