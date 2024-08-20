from django.db import models
#from django.contrib.auth.models import User

# models de la base de datos de una app de control de stock

class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Name')
    description = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Description')
    stock = models.IntegerField(null=False, blank=False, verbose_name='Stock')
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Name')
    description = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Description')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
