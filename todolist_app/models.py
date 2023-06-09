from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'{self.task.title()} - {self.done}'
    
# Create your models here.
