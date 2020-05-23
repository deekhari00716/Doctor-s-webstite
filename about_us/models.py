from django.db import models

class About(models.Model):
    img = models.ImageField(upload_to='home/images')
    info = models.TextField()
    resume = models.FileField(upload_to='home/images')
    bio = models.TextField(blank=True)

    
