from this import s
from django.db import models

# Create your models here.



class SiteModel(models.Model):
    name = models.CharField(max_length=40,blank=True,null=True)
    category = models.CharField(max_length=40,blank=True,null = True)
    is_available = models.BooleanField(default=False,blank=True,null=True)
    slug = models.SlugField(max_length=40,null=True,unique=True)


    def __str__(self):
        return self.name