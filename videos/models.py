from django.db import models

class Youtube_video(models.Model):
    name = models.CharField(max_length=128,blank=True)
    url= models.URLField(blank=True)
    date_published=models.DateTimeField(auto_now=False,auto_now_add=False,null=True)


## Table for the youtube autosheduled jobs
class Media(models.Model):
    class Meta :
        verbose_name_plural='Media'

    timestamp=models.DateTimeField(auto_now_add=True)
    video_id=models.CharField(max_length=20,unique=True)
    title=models.CharField(max_length=200)
    duration=models.CharField(max_length=20)
    iframe=models.CharField(max_length=2000)
    description=models.CharField(max_length=2000)
    
    image=models.URLField()
    
    is_active=models.BooleanField(default=True)

    class Meta:
        ordering=["timestamp"]

