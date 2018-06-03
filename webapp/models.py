from django.db import models

class Restuarant(models.Model):
    name = models.CharField(max_length=100)

    def add(self):
        self.save()

    def __str__(self):
        return self.name
