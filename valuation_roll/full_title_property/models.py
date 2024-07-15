from django.db import models


class Property(models.Model):
    rate_number = models.CharField(max_length=50)
    legal_description = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title_number
