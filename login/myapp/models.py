from django.db import models

# Create your models here.
class signup(models.Model):
    title=models.CharField(max_length=50,null=False)
    description=models.CharField(max_length=150,null=False)