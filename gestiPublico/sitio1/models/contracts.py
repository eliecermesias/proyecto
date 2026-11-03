from django.db import models

class contracts(models.Model):
    code = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    people_id = models.ForeignKey('people', on_delete=models.RESTRICT, null=True, blank=True)
    property_id = models.ForeignKey('properties', on_delete=models.RESTRICT, null=True, blank=True)
    provider_id = models.ForeignKey('providers', on_delete=models.RESTRICT, null=True, blank=True)
    invoices = models.ManyToManyField('invoices', related_name='contracts', blank=True)

    def __str__(self):
        return self.code