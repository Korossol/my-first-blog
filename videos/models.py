from django.db import models

class Youtube_video(models.Model):
    name = models.CharField(max_length=128,blank=True)
    url= models.URLField(blank=True)
    date_published=models.DateTimeField(auto_now=False,auto_now_add=False,null=True)


    

