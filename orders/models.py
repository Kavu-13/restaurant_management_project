from django.db import models
from .utils import generate_coupon_code

class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True, blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_coupon_code()
        super().save(*args, **kwargs)
