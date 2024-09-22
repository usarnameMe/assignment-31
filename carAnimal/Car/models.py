from django.db import models


class Car(models.Model):
    objects = None
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.make}{self.model}{self.year}"
