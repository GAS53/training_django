from tabnanny import verbose
from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(null=True, blank=True, max_length=200)
    price = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=2)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')


    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']

    def __str__(self):
        return self.name