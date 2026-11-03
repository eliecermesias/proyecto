from django.db import models


class people(models.Model):
    Name = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.Name
