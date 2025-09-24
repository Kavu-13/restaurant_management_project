from django.db import models

# Create your models here.
 class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = odels.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_length=8, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name