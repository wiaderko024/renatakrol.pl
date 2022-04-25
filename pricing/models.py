from django.db import models


class Price(models.Model):
    price = models.TextField(default="", blank=False, null=False)

    def __str__(self):
        return self.price
