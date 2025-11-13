from django.db import models

class Category(models.Model):
    name = models.CharField(max_length= 200)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description  = models.TextField(blank=True)
    price = models.DecimalField(max_digits=200, decimal_places=2, default=0.00)
    
    def __str__(self):
        return self.name