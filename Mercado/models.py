from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class mall(models.Model):
    nombre = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
        
class tienda(models.Model):
    nombre = models.CharField(max_length=50)
    mall = models.ForeignKey(mall, on_delete=CASCADE)

    def __str__(self):
        return self.nombre
        
class producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits = 7, decimal_places = 2)
    tienda = models.ForeignKey(tienda, on_delete=CASCADE)

    def __str__(self):
        return self.nombre
