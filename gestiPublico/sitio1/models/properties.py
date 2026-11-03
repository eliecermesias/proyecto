from django.db import models


class properties(models.Model):
    code = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Context = models.TextField()
    people_Id = models.ForeignKey('people', on_delete=models.RESTRICT, null=True, blank=True)

    def __str__(self):
        return self.code
