from django.db import models


# Create your models here.

class PagesToScan(models.Model):
    url = models.URLField(max_length=500)

    def __str__(self):
        return str(self.url)
