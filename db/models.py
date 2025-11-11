import sys
try:
    from django.db import models
except Exception:
    print('Django not installed. Run: pip install django')
    sys.exit()

class User(models.Model):
    name = models.CharField(max_length=50, default="Dan")

    def __str__(self):
        return self.name

class Product(models.Model):
    upc = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} - ${self.price}"

