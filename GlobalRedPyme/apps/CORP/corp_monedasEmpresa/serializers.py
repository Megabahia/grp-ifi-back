from rest_framework import serializers

from apps.CORP.corp_monedasEmpresa.models import (
    MonedasEmpresa
)

class MonedasEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonedasEmpresa
        fields = '__all__'
        read_only_fields = ['_id']
