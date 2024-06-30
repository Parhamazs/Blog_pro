from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-publish',)
        indexes = [
            models.Index(fields=['title', 'publish', 'created', 'updated'])
        ]
    
    def __str__(self):
        return self.title  
    
    
    
