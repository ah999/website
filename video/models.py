from django.db import models

# Create your models here.
class Video(models.Model):
    video_title = models.CharField(max_length=100)
    video_url = models.CharField(max_length=1000)
    def __str__(self):
        return self.video_title
