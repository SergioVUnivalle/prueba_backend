from django.contrib.gis.db import models
from django.utils import timezone

class Municipio(models.Model):
    geom = models.MultiPolygonField(srid=4326,null=True, blank=True)
    municipio = models.CharField(max_length=50,null=True, blank=True)
    dpto = models.CharField(max_length=60,null=True, blank=True)
    disposicion = models.CharField(max_length=60,null=True, blank=True)
    cod_dane = models.CharField(max_length=60,null=True, blank=True)
    created_date = models.DateTimeField(max_length=60,default=timezone.now) 

    def __str__(self):
        return self.municipio


class Oficina(models.Model):
    geom = models.PointField(srid=4326,null=True, blank=True)
    gid = models.BigIntegerField(null=True, blank=True)
    nombre = models.CharField(max_length=254,null=True, blank=True)
    departamen = models.CharField(max_length=254,null=True, blank=True)
    municipio = models.CharField(max_length=254,null=True, blank=True)

    def __str__(self):
        return self.nombre
