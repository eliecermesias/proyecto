from django.db import models

class providers(models.Model):
    Name = models.CharField(max_length=100)
    Nit = models.CharField(max_length=20)
    Phone = models.CharField(max_length=20)
    Origin = models.CharField(max_length=100)
    Owner = models.CharField(max_length=100)
    IsActive = models.BooleanField(default=True)

def __str__(self):
    return self.Name