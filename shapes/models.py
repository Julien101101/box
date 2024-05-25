import datetime

from django.db import models
from django.utils import timezone


class Shape(models.Model):
    def __str__(self):
        return self.shape_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Topic(models.Model):
    "A topic the user is learning about."
    text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField("date published")#(auto_now_add = True)

    def __str__(self):
        "Return a string representation of the model."
        return self.text

class Home(models.Model):
    pass
