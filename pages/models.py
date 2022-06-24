from django.db import models

# Create your models here.


class Contact(models.Model):
    username = models.CharField(max_length=30,null=True)
    email = models.EmailField(max_length=30,null=True)
    message = models.TextField(max_length=200,null=True)

    def __str__(self):
        return self.username

    

