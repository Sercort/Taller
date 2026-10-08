from django.contrib import admin

# Register your models here.s
from .models import Cliente, Reparacion, Costo

admin.site.register(Cliente)
admin.site.register(Reparacion)
admin.site.register(Costo)