from django.db import models

class Profile(models.Model):
    username = models.CharField(max_length=50 )
    email = models.EmailField(unique=True)
    profile_pic = models.ImageField(upload_to='images/%Y/%m/%d',null=True)
    resume= models.FileField(upload_to='resume/',null=True)

    def __str__(self):
        return self.username
