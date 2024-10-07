from django.urls import reverse
from django.db import models

from  django.conf import settings
# from django.contrib.auth.models import User
# from django.urls import reverse
# from core import settings      # another way to call  settings.py
class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   
    title = models.CharField(max_length=200)
    content = models.TextField()  # Ensure this is defined
    def  __str__(self):
       return self.title
    def get_absolute_url(self):
        return reverse("post_detail",kwargs={"blog_id" : self.id})
    
    # def get_update_url(self):
    #     return reverse("update_post",kwargs={"post_id" : self.id})
    
    # def get_delete_url(self):
    #     return reverse("delete_item",kwargs={"item_id" : self.id})
    
# Create your models here.
     # auther = models.ForeignKey(User)  # ANOTHER WAY TO ADD A FOREGIN KEY PARAMETER
      # auther = models.ForeignKey("auth.user")  # ANOTHER WAY TO ADD A FOREGIN KEY PARAMETER