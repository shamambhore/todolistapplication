from statistics import mode
from django.db import models

# Create your models here.

class Task(models.Model):
    task_title = models.CharField(max_length=30)
    task_desc = models.TextField()
    task_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.task_title
    
