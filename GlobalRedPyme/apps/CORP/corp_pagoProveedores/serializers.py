from rest_framework import serializers

from .models import (
    PagoProveedores
)

class PagoProveedorSerializer(serializers.ModelSerializer):
    # La clase meta se relaciona con la tabla PagoProveedores
    # el campo fields indica los campos que se devolveran
    class Meta:
        model = PagoProveedores
        fields = '__all__'
        read_only_fields = ['_id']
