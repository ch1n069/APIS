from django.db import models
import datetime

# Create your models here.

# use email and password rather using password/username



class User(models.Model):
    

    created_at = models.DateTimeField(auto_now_add=True)