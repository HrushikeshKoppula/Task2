from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)


class Satellite(models.Model):
    OBJECT_NAME = models.CharField(max_length=25, null=True)
    OBJECT_ID = models.CharField(max_length=10, null=True)
    EPOCH = models.DateTimeField(null=True)
    MEAN_MOTION = models.FloatField(null=True)
    ECCENTRICITY = models.FloatField(null=True)
    INCLINATION = models.FloatField(null=True)
    RA_OF_ASC_NODE = models.FloatField(null=True)
    ARG_OF_PERICENTER = models.FloatField(null=True)
    MEAN_ANOMALY = models.FloatField(null=True)
    EPHEMERIS_TYPE = models.IntegerField(null=True)
    CLASSIFICATION_TYPE = models.CharField(max_length=1, null=True)
    NORAD_CAT_ID = models.IntegerField(null=True)
    ELEMENT_SET_NO = models.IntegerField(null=True)
    REV_AT_EPOCH = models.IntegerField(null=True)
    BSTAR = models.FloatField(null=True)
    MEAN_MOTION_DOT = models.FloatField(null=True)
    MEAN_MOTION_DDOT = models.FloatField(null=True)


    # "OBJECT_NAME":"CALSPHERE 1",
    # "OBJECT_ID":"1964-063C",
    # "EPOCH":"2024-05-04T13:40:23.299968",
    # "MEAN_MOTION":13.74964535,
    # "ECCENTRICITY":0.0027986,
    # "INCLINATION":90.2049,
    # "RA_OF_ASC_NODE":54.443,
    # "ARG_OF_PERICENTER":108.3821,
    # "MEAN_ANOMALY":66.6978,
    # "EPHEMERIS_TYPE":0,
    # "CLASSIFICATION_TYPE":"U",
    # "NORAD_CAT_ID":900,
    # "ELEMENT_SET_NO":999,
    # "REV_AT_EPOCH":96503,
    # "BSTAR":0.00095764,
    # "MEAN_MOTION_DOT":9.25e-6,
    # "MEAN_MOTION_DDOT":0