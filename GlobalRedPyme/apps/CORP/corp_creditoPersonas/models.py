import jsonfield
from djongo import models

def upload_path(instance, filname):
    return '/'.join(['CORP/documentosCreditosPersonas', str(instance._id) + "_" + filname])

# Create your models here.
class CreditoPersonas(models.Model):
    _id = models.ObjectIdField()
    numero = models.IntegerField(blank=True, null=True)
    canal = models.CharField(max_length=255,blank=True, null=True)
    monto = models.FloatField(blank=True, null=True)
    montoAprobado = models.FloatField(blank=True, null=True)
    gastosAdministrativos = models.FloatField(blank=True, null=True)
    montoLiquidar = models.FloatField(blank=True, null=True)
    cuota = models.FloatField(blank=True, null=True)
    plazo = models.PositiveIntegerField(blank=True, null=True)
    aceptaTerminos = models.SmallIntegerField(default=1)
    estado = models.CharField(max_length=255,blank=True, null=True)
    user_id = models.CharField(max_length=255,blank=True, null=True)  # Relacion usuario
    empresaComercial_id = models.CharField(max_length=255,blank=True, null=True)  # Relacion empresa comercial
    empresaIfis_id = models.CharField(max_length=255,blank=True, null=True)  # Relacion empresa ifis
    reporteBuro = models.FileField(blank=True,null=True,upload_to=upload_path)
    calificacionBuro = models.CharField(max_length=255,blank=True, null=True)
    buroValido = models.CharField(max_length=255,blank=True, null=True)
    identificacion = models.FileField(blank=True,null=True,upload_to=upload_path)
    papeletaVotacion = models.FileField(blank=True,null=True,upload_to=upload_path)
    identificacionConyuge = models.FileField(blank=True,null=True,upload_to=upload_path)
    papeletaVotacionConyuge = models.FileField(blank=True,null=True,upload_to=upload_path)
    planillaLuzNegocio = models.FileField(blank=True,null=True,upload_to=upload_path)
    planillaLuzDomicilio = models.FileField(blank=True,null=True,upload_to=upload_path)
    facturas = models.FileField(blank=True,null=True,upload_to=upload_path)
    matriculaVehiculo = models.FileField(blank=True,null=True,upload_to=upload_path)
    impuestoPredial = models.FileField(blank=True,null=True,upload_to=upload_path)
    buroCredito = models.FileField(blank=True,null=True,upload_to=upload_path)
    evaluacionCrediticia = models.FileField(blank=True,null=True,upload_to=upload_path)
    ruc = models.FileField(blank=True,null=True,upload_to=upload_path)
    rolesPago = models.FileField(blank=True,null=True,upload_to=upload_path)
    panillaIESS = models.FileField(blank=True,null=True,upload_to=upload_path)
    mecanizadoIess = models.FileField(blank=True,null=True,upload_to=upload_path)
    fotoCarnet = models.FileField(blank=True,null=True,upload_to=upload_path)
    solicitudCredito = models.FileField(blank=True,null=True,upload_to=upload_path)
    evaluacionCrediticia = models.FileField(blank=True,null=True,upload_to=upload_path)
    buroCreditoIfis = models.FileField(blank=True,null=True,upload_to=upload_path)
    pagare = models.FileField(blank=True,null=True,upload_to=upload_path)
    contratosCuenta = models.FileField(blank=True,null=True,upload_to=upload_path)
    tablaAmortizacion = models.FileField(blank=True,null=True,upload_to=upload_path)
    codigoClienteCreado = models.CharField(max_length=255,null=True, blank=True)
    codigoCuentaCreada = models.CharField(max_length=255,null=True, blank=True)
    calificacionBuroIfis = models.CharField(max_length=255,null=True, blank=True)
    tomarSolicitud = models.CharField(max_length=255,null=True, blank=True)
    fechaAprobacion = models.DateTimeField(null=True, blank=True)
    tipoCredito = models.CharField(max_length=255,null=True, blank=True)
    concepto = models.CharField(max_length=255,null=True, blank=True)
    documentoAprobacion = models.FileField(blank=True,null=True,upload_to=upload_path)
    empresasAplican = models.TextField(null=True, blank=True)
    vigencia = models.DateField(null=True, blank=True)
    interes = models.FloatField(null=True, blank=True)
    nombres = models.CharField(max_length=255,blank=True, null=True)
    apellidos = models.CharField(max_length=255,blank=True, null=True)
    nombresCompleto = models.CharField(max_length=255,blank=True, null=True)
    fechaAprobado = models.DateField(null=True, blank=True)
    numeroIdentificacion = models.CharField(max_length=255,blank=True, null=True)
    codigoCliente = models.CharField(max_length=255,blank=True, null=True)
    codigoCorp = models.CharField(max_length=255,blank=True, null=True)
    numeroFactura = models.CharField(max_length=255,blank=True, null=True)
    montoVenta = models.CharField(max_length=255,blank=True, null=True)
    checkPagare = models.BooleanField(blank=True, null=True)
    checkTablaAmortizacion = models.BooleanField(blank=True, null=True)
    checkManualPago = models.BooleanField(blank=True, null=True)
    checkCedula = models.BooleanField(blank=True, null=True)
    external_id = models.CharField(max_length=255,blank=True, null=True)
    montoDisponible = models.FloatField(null=True, blank=True)
    codigoPreaprobado = models.CharField(max_length=255,null=True, blank=True)
    tipoPersona = models.CharField(max_length=255,null=True, blank=True)
    estadoCivil = models.CharField(max_length=255,null=True, blank=True)

    user = jsonfield.JSONField()
    observacion = models.TextField(null=True, blank=True)

    checks = jsonfield.JSONField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)

class AutorizacionCredito(models.Model):
    _id = models.ObjectIdField()
    codigo = models.CharField(max_length=200,null=False)
    credito = models.CharField(max_length=250,blank=False, null=False)  # Relacion credito persona
    entidad = models.CharField(max_length=250,blank=False, null=False)  # Entidad hace referencina a si es una persona o una empresa se guarda el id

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)

class LecturaArchivos(models.Model):
    _id = models.ObjectIdField()
    numeroCredito = models.CharField(max_length=200,null=False) # Relacion credito persona
    identificacion = models.CharField(max_length=250,blank=False, null=False)
    ruc = models.CharField(max_length=250,blank=False, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    state = models.SmallIntegerField(default=1)