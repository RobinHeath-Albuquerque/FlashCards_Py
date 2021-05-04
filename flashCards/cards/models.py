from django.db import models


class FlashCards(models.Model):
    code = models.CharField(max_length=50)
    definition = models.CharField(max_length=100)
    collection = models.ForeignKey('Collection', default=None, null=True, on_delete=models.CASCADE)


class Collection(models.Model):
    title = models.CharField(max_length=50)

# Create your models here.
