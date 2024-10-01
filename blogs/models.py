
from django.db import models
# from core import settings      # another way to call  settings.py
from  django.conf import settings
# from django.contrib.auth.models import User
# from django.urls import reverse

class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # auther = models.ForeignKey(User)  # ANOTHER WAY TO ADD A FOREGIN KEY PARAMETER
    # auther = models.ForeignKey("auth.user")  # ANOTHER WAY TO ADD A FOREGIN KEY PARAMETER
    title = models.CharField(max_length=200)
    content = models.TextField()  # Ensure this is defined
    def  __str__(self):
       return self.title

# Create your models here.
