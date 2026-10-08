from django.db import models

# Create your models here.

class Cliente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.rut})"


class Reparacion(models.Model):
    ESTADO_CHOICES = [
        ('ingresado', 'Ingresado'),
        ('en_proceso', 'En Proceso'),
        ('completado', 'Completado'),
        ('entregado', 'Entregado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vehiculo_o_equipo = models.CharField(max_length=100)
    descripcion_falla = models.TextField()
    fecha_ingreso = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='ingresado')

    def __str__(self):
        return f"Reparación #{self.id} - {self.vehiculo_o_equipo} ({self.cliente.nombre})"


class Costo(models.Model):
    reparacion = models.OneToOneField(Reparacion, on_delete=models.CASCADE)
    monto_mano_obra = models.IntegerField(default=0)
    monto_repuestos = models.IntegerField(default=0)
    monto_total = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.monto_total = self.monto_mano_obra + self.monto_repuestos
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Costo Reparación #{self.reparacion.id}: ${self.monto_total}"