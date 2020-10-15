from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class HostData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tournament_name = models.CharField(max_length=30)
    maps = models.CharField(max_length=10)
    team = models.CharField(max_length=7)
    perspective = models.CharField(max_length=4)
    price = models.IntegerField()
    ranks = models.IntegerField()
    amount_kill = models.IntegerField()


    def __str__(self):
        return self.tournament_name
    

