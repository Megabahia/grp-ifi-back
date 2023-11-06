"""Nube: Bigpuntos
PORTALES: CENTER, PERSONAS
"""

from rest_framework import serializers

from .models import (
    Correos
)


# Esta clase se usa para comunicarse con la tabla de Correos landing
class CorreosSerializer(serializers.ModelSerializer):
    # el campo model conecta con la tabla de correos
    # el campo fields retorna todos los campos de la tabla correos
    class Meta:
        model = Correos
        fields = '__all__'
