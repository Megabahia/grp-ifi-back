from rest_framework import serializers

from apps.CORP.corp_cobrarSupermonedas.models import (
    CobrarSupermonedas
)

class CobrarSupermonedasSerializer(serializers.ModelSerializer):
    class Meta:
        model = CobrarSupermonedas
       	fields = '__all__'
        read_only_fields = ['_id']
