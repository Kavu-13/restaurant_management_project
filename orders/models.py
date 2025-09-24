from django.db import models
from django.contrib.auth.models import User


class ActiveOrderManager(models.Manager):
    def get_active_orders(self):
        # filter based on OrderStatus.name
        return super().get_queryset().filter(status__name__in=['pending', 'processing'])

# Create your models here.
class OrderStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    # example field for your Order model
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    customer_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # Attach custom manager
    objects = ActiveOrderManager()

    def __str__(self):
        return f"Order #{self.id} -- {self.customer_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product_name} (x{self.quantity})"



