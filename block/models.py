from django.db import models
 

class Author(models.Model):
    
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=200)
   
     



# Create your models here.
