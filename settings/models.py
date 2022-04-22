from django.db import models

# Create your models here.


class Currency(models.Model):
    code = models.CharField(max_length=10,unique=True, default="AED")
    desc = models.CharField(max_length=20,default="United Arab Emirates Dirham")
    cost = models.CharField(max_length=20,default="1")

    def __str__(self):
        return self.code