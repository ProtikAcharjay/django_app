from django.db import models
from django.utils import timezone

# Create your models here.
class ProItems(models.Model):
    ITEM_TYPE_CHOICES = [
        ('Car', 'Car'),
        ('Product', 'Product'),
        ('Docuement', 'Docuement'),
        ('Other', 'Other'),
    ]
    name = models.CharField(max_length=255)
    price = models.IntegerField(null=True)
    address = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='proImages/')
    description = models.TextField(blank=True)
    timezone = models.DateTimeField(default=timezone.now)
    item_type = models.CharField(max_length=11,choices=ITEM_TYPE_CHOICES)

    def __str__(self):
        return self.name
