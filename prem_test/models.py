from django.db import models

# Create your models here.
class premier_users(models.Model):
    names=models.CharField(max_length=32,null=True)
    status=models.CharField(max_length=32,null=True)
    title=models.CharField(max_length=32,null=True)
    email= models.CharField(max_length=20,default='', null=True)
    branch_key= models.CharField(max_length=32, null=True, default='')

    # def __str__(self):
    #     return self.email