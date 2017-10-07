from django.db import models
from datetime import datetime

class temp_read(models.Model):

    temp = models.CharField(max_length=5)
    dt = models.DateTimeField(default=datetime.now(),)

    def __str__(self):
        return str(self.temp)


class water_level(models.Model):
    ON='1'
    OFF='0'
    choices_yes_or_no=(( ON ,"YES"), ( OFF , "OFF"))
    level=models.CharField(max_length=5)
    is_on= models.CharField(max_length=3,choices=choices_yes_or_no)


class soil_moisture(models.Model):
    m_level = models.CharField(max_length=5)
    dt = models.DateTimeField(default=datetime.now(), )



