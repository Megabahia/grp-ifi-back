from rest_framework import serializers

from .models import (
    MovimientoCobros
)


class MovimientoCobrosSerializer(serializers.ModelSerializer):
    # La clase meta se relaciona con la tabla MovimientoCobros
    # el campo fields indica los campos que se devolveran
    # el campo read_only_fields
    class Meta:
        model = MovimientoCobros
        fields = '__all__'
        read_only_fields = ['_id']
