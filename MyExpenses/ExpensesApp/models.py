from django.db import models


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    budget = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.budget}$ {self.last_name}'


class Expense(models.Model):
    title = models.CharField(max_length=50)
    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
