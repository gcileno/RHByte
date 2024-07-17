from rest_framework import serializers
from .models import Vagas, CandidaturaSimples

class VagasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vagas
        fields = '__all__'

class CadidaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidaturaSimples
        fields = '__all__'