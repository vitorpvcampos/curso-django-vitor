from django.contrib.auth import get_user_model
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    start = models.DateField()
    end = models.DateField()
    students = models.ManyToManyField(get_user_model(), through='Subscription')


class Subscription(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['user', 'team']]
        ordering = ['team', 'date']
