from django.db import models

# Create your models here.
class Review(models.Model):

    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self) -> str:
        return self.product.name
