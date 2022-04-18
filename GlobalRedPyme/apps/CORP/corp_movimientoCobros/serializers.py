from rest_framework import serializers

from apps.CORP.corp_movimientoCobros.models import (
    MovimientoCobros
)

class MovimientoCobrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimientoCobros
       	fields = '__all__'
        read_only_fields = ['_id']
