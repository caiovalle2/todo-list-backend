from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    description = models.CharField(max_length=255)

    deadline = models.DateField()

    is_done = models.BooleanField(default=False)
    
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Task {self.id}: {self.description}"