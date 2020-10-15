from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mob_no = models.CharField(max_length=10)
    ref_code = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.mob_no 



