from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.


class Look(models.Model):
    shape = models.CharField(max_length=20)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.shape}, {self.color}'

    def get_absolute_url(self):
        return reverse('looks_detail', kwargs={'pk': self.id})


class Magnet(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    date = models.IntegerField()
    looks = models.ManyToManyField(Look)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'magnet_id': self.id})


class Review(models.Model):
    date = models.DateField('review date')
    review = models.TextField(max_length=250)
    magnet = models.ForeignKey(Magnet, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.review} - {self.date}'

    class Meta:
        ordering = ['date']
