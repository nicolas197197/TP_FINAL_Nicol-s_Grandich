from django.db import models

class Basquet(models.Model):
    numeroDeSocio = models.IntegerField()
    nombre=models.CharField(max_length=40)
    fechaDeIngreso = models.DateField() 
    email = models.EmailField()

    def __str__(self):
        return f'Nombre del basquetbolista: {self.nombre} / {self.email} --'