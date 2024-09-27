
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()  # Ensure this is defined

# Create your models here.
