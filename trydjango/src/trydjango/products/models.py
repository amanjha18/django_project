from django.db import models

# Create your models here.
class Product(models.Model):
    title         = models.CharField(max_length=120) #max_length = required
    description   = models.TextField(blank=True, null=True) #field is optional to all circumstances.
    price         = models.IntegerField()
    summary       = models.TextField(blank=False, null=False) #value is required in all circumstances.
    featured      = models.BooleanField(default=False) #null=True, default=True
