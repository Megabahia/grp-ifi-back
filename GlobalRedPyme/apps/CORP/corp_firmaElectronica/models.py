from djongo import models


# Create your models here.
class FirmaElectronica(models.Model):
    _id = models.ObjectIdField()
    nombreRepresentante = models.CharField(max_length=255, null=True, blank=True)
    apellidoRepresentante = models.CharField(max_length=255, null=True, blank=True)
    correoRepresentante = models.CharField(max_length=255, null=True, blank=True)
    telefonoRepresentante = models.CharField(max_length=255, null=True, blank=True)
    whatsappRepresentante = models.CharField(max_length=255, null=True, blank=True)
    cedulaRepresentante = models.CharField(max_length=255, null=True, blank=True)
    archivo = models.CharField(max_length=255, null=True, blank=True)
    user_id = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)
