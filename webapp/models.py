from django.db import models

# Create your models here.

class Restuarant(models.Model):
    name = models.CharField(max_length=100)

    def add(self):
        self.save()

    def __str__(self):
        return self.name
