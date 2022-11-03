from re import I
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Product(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    product_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.product_name}"
        
@receiver(post_save, sender=User)
def product_create(sender, instance, created, **kwargs):
    if created:
        Product.objects.create(user=instance)
        print('Product created')

@receiver(post_save, sender=User)
def product_update(sender, instance, created, **kwargs):
    if created == False:
        instance.product.save()
        print('Product updated')
