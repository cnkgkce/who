from django.db import models

# Create your models here.



class Site(models.Model):
    name = models.CharField(max_length=40,blank=True,null=True)
    category = models.CharField(max_length=40,blank=True,null = True)
    image = models.ImageField(upload_to='sites/',default='sites/default.jpg',blank=True,null=True)
    url = models.CharField(max_length=1000,blank=True,null=True,default='https://google.com')
    is_available = models.BooleanField(default=False,blank=True,null=True)
    slug = models.SlugField(max_length=40,null=True,unique=True)


    def __str__(self):
        return self.name