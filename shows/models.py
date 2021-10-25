from django.db import models
import datetime

class ShowManager(models.Manager):
   def validator(self, postData):
      errors = {}
      if len(postData['title']) < 2:
         errors["title"] = "Title of show should be at least 2 characters"
      if len(postData['network']) < 3:
         errors["network"] = "Name of Network should be at least 3 characters"
      if len(postData['desc']) < 10 and len(postData['desc']) != 0:
         errors["desc"] = "Description should be either empty or at least 10 characters"
      return errors

class Show(models.Model):
   title = models.CharField(max_length=255)
   network = models.CharField(max_length=50)
   reldate = models.DateField()
   desc = models.TextField(null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   objects = ShowManager()