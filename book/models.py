from django.db import models
from django.core.urlresolvers import reverse


class Book(models.Model):
    isbn = models.IntegerField(primary_key=True)
    logo = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)
    favorite = models.BooleanField(default=False)

    def get_absolute_url(self) :
        return reverse('book : detail', kwargs = {'pk': self.pk})

    def __str__(self) :
        return self.title + " - " + self.author


