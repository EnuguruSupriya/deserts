from django.db import models
class Menu(models.Model):
    brand=models.CharField(max_length=20)
    flovour=models.CharField(max_length=30)
    quantity=models.IntegerField()
    price=models.IntegerField()
def __str__(self):
    return self.brand
