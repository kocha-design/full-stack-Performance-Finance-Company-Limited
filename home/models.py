from django.db import models
from django.utils import timezone

class GalleryImage(models.Model):
    title = models.CharField(max_length=200,default= 'Image Title')
    image = models.ImageField(upload_to='gallery/',default='2.jpg')
    caption = models.TextField(blank=True, default='Image Caption')
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)
    order = models.IntegerField(default=1)
    
    class Meta:
        ordering = ['order', '-created_date']
    
    def __str__(self):
        return self.title