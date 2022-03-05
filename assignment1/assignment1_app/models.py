from django.db import models

# Create your models here.
class CoffeeRoaster(models.Model):
    name = models.CharField(max_length = 256)
    farm = models.CharField(max_length = 256)
    region = models.CharField(max_length = 256)
    fermentation = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name
