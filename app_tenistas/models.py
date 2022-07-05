from django.db import models

class Tenis(models.Model):
    numeroDeSocio = models.IntegerField()
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    fechaDeIngreso = models.DateField() 
    email = models.EmailField()
    descripcion = models.TextField(blank = True, null=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido} --'