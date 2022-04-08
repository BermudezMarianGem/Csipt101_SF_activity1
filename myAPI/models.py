from django.db import models

# Create your models here.

class vehicls(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=100)

    def __str__ (self):
        return self.name