from django.db import models

from authors.models import Author


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField("Tag", blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    published_date = models.DateField()

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
