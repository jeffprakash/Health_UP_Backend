from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User=get_user_model()

class Profile(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.TextField(blank=False)
    age = models.IntegerField(blank=True,null=True)
    height = models.IntegerField(blank=True,null=True)
    weight = models.IntegerField(blank=True,null=True)
    prevcondition = models.TextField(blank=True,null=True)
    medication = models.TextField(blank=True,null=True)
    img= models.ImageField(upload_to='pics',default='default-user.png')
    location=models.CharField(max_length=100,blank=True,null=True)
    


    def __str__(self):
        return self.user.username