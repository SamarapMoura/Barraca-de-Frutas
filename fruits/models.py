from django.db import models

class Fruit(models.Model):
    classification_options = (
        ('EX', 'Extra'),
        ('1ST', 'Primeira'),
        ('2ND', 'Segunda'),
        ('3RD', 'Terceira')
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, unique=True)
    fresh = models.BooleanField()
    stock = models.PositiveIntegerField()
    price = models.FloatField()
    classification = models.CharField(max_length=3, choices=classification_options)
    def __str__(self):
        return self.name