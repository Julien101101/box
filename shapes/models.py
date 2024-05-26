import datetime

from django.db import models
from django.utils import timezone


class Shape(models.Model):
    shape_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField("date published") #(auto_now_add = True)

    def __str__(self):
        return self.shape_text

