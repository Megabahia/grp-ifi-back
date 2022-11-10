from djongo import models
from django.utils import timezone


def upload_path(instance, filname):
    return '/'.join(['CORP/documentosCreditosArchivos', str(timezone.localtime(timezone.now())) + "_" + filname])


def upload_path2(instance, filname):
    return '/'.join(['CORP/archivosFirmados', str(timezone.localtime(timezone.now())) + "_" + filname])


# Create your models here.
class PreAprobados(models.Model):
    fechaCargaArchivo = models.DateField(null=True)
    campania = models.CharField(max_length=255, null=True, blank=True)
    registrosCargados = models.CharField(max_length=255, null=True, blank=True)
    linkArchivo = models.FileField(blank=True, null=True, upload_to=upload_path)
    tamanioArchivo = models.CharField(max_length=255, null=True, blank=True)
    usuarioCargo = models.CharField(max_length=255, null=True, blank=True)
    user_id = models.CharField(max_length=255, null=True, blank=True)  # Relacion de usuario
    tipoCredito = models.CharField(max_length=255, null=True, blank=True)
    empresa_financiera = models.CharField(max_length=255, null=True, blank=True)
    empresa_comercial = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)

    def save(self, *args, **kwargs):
        return super(PreAprobados, self).save(*args, **kwargs)


class ArchivosFirmados(models.Model):
    _id = models.ObjectIdField()
    solicitudCredito = models.FileField(blank=True, null=True, upload_to=upload_path2)
    evaluacionCrediticia = models.FileField(blank=True, null=True, upload_to=upload_path2)
    buro = models.FileField(blank=True, null=True, upload_to=upload_path2)
    identificacion = models.FileField(blank=True, null=True, upload_to=upload_path2)
    papeletaVotacion = models.FileField(blank=True, null=True, upload_to=upload_path2)
    identificacionConyuge = models.FileField(blank=True, null=True, upload_to=upload_path2)
    papeletaVotacionConyuge = models.FileField(blank=True, null=True, upload_to=upload_path2)
    planillaLuzDomicilio = models.FileField(blank=True, null=True, upload_to=upload_path2)
    mecanizadoIees = models.FileField(blank=True, null=True, upload_to=upload_path2)
    matriculaVehiculo = models.FileField(blank=True, null=True, upload_to=upload_path2)
    impuestoPredial = models.FileField(blank=True, null=True, upload_to=upload_path2)
    autorizacionInformacion = models.FileField(blank=True, null=True, upload_to=upload_path2)
    fichaCliente = models.FileField(blank=True, null=True, upload_to=upload_path2)
    conveniosCuenta = models.FileField(blank=True, null=True, upload_to=upload_path2)
    pagare = models.FileField(blank=True, null=True, upload_to=upload_path2)
    tablaAmortizacion = models.FileField(blank=True, null=True, upload_to=upload_path2)
    seguroDesgravamen = models.FileField(blank=True, null=True, upload_to=upload_path2)
    gastosAdministracion = models.FileField(blank=True, null=True, upload_to=upload_path2)
    numeroIdentificacion = models.CharField(max_length=255, blank=False, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)
