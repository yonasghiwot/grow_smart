from django.db import models


# Create your models here.
from django.db import models

class SensorsData(models.Model):

    TimeStamp = models.DateTimeField(auto_now_add=True)
    Temprature = models.CharField(max_length=4)
    Humidity = models.CharField(max_length=4)
    PH = models.CharField(max_length=5)
    EC =models.CharField(max_length=4)

class ControlParameters(models.Model):
    
    TimeStamp = models.DateTimeField(auto_now_add=True)
    Temperature_Max = models.CharField(max_length=5)
    Temperature_Min = models.CharField(max_length=5)
    Humidity_Max = models.CharField(max_length=5)
    Humidity_Min = models.CharField(max_length=5)
    PH_Max = models.CharField(max_length=5)
    PH_Min = models.CharField(max_length=5)
    EC_Max = models.CharField(max_length=5)
    EC_Min = models.CharField(max_length=5)
    Light_Max = models.CharField(max_length=5)
    Light_Min = models.CharField(max_length=5)

class Relays(models.Model):

    TimeStamp = models.DateTimeField(auto_now_add=True)
    Relay1 = models.BooleanField()
    Relay2 = models.BooleanField()
    Relay3 = models.BooleanField()
    Relay4 = models.BooleanField()
    Relay5 = models.BooleanField()
    Relay6 = models.BooleanField()
    Relay7 = models.BooleanField()
    Relay8 = models.BooleanField()

class DutchBucketOne(models.Model):

    TimeStamp = models.DateTimeField(auto_now_add=True)
    FirstFeedStart = models.TimeField()
    SecondFeedStart = models.TimeField()
    ThirdFeedStart = models.TimeField()
    FeedDuration = models.CharField(max_length=3)

class DutchBucketTwo(models.Model):

    TimeStamp = models.DateTimeField(auto_now_add=True)
    FirstFeedStart = models.TimeField()
    SecondFeedStart = models.TimeField()
    ThirdFeedStart = models.TimeField()
    FeedDuration = models.CharField(max_length=3)

class SeedlingControl(models.Model):

    TimeStamp = models.DateTimeField(auto_now_add=True)
    FirstFeedStart = models.TimeField()
    SecondFeedStart = models.TimeField()
    ThirdFeedStart = models.TimeField()
    FeedDuration = models.CharField(max_length=3)
