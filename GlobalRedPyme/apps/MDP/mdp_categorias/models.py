from django.db import models


# Mundo: bigpuntos
# Portales: Corp
# Esta clase sirve para relacionar la tabla de las categorias de la base datos mdp
class Categorias(models.Model):
    nombre = models.CharField(max_length=255, null=False)
    codigoCategoria = models.CharField(max_length=150, null=False)
    descripcion = models.TextField(null=True)
    estado = models.CharField(max_length=150, null=False, default="Inactivo")
    # Id de la empresa que se inicia sesion
    empresa_id = models.CharField(max_length=255, null=False, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)
