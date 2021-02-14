

# Create your models here.
from django.db import models

# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '{}'.format(self.search)

    """ au lieu d'enregistrer l'objet crée sous le nom object 1 il sera enregistrée par son nom réel déterminée par l'attribut search"""

    class Meta:
        verbose_name_plural = 'Searches'
