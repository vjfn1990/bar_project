from django.db import models

# Create your models here.

class Beer(models.Model):
    ref = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Counter(models.Model):
    members = models.ManyToManyField(Beer, through='Membership')
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Membership(models.Model):
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)
    counter = models.ForeignKey(Counter, on_delete=models.CASCADE)
    availability = models.IntegerField(default=0)
    def __str__(self):
        return str(self.availability)
