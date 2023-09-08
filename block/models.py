from django.db import models
 

class Author(models.Model):
    
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=200)
    
    image=models.ImageField( upload_to='Author/',blank=True, null=True)
   
     



# Create your models here.
