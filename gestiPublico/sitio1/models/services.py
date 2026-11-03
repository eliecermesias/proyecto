from django.db import models

class services(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.TextField()
    IsActive = models.BooleanField(default=True)

def __str__(self):
    return self.Name