from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(null=True, blank=True, max_length=200)
    price = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=2)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
