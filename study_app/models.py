from django.db import models

# Create your models here.

class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    review_text = models.TextField()

    def __str__(self):
        return self.name


class Review1(models.Model):
    email = models.EmailField()