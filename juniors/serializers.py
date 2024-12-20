from rest_framework import serializers
from .models import EmpresasJuinior, Voluntario, Membro, Funcao, HistoricoMembro, Departamento, Informacoes

class JuniorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresasJuinior
        fields = '__all__'

class VoluntarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voluntario
        fields = '__all__'

class MembroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membro
        fields = '__all__'

class FuncaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcao
        fields = '__all__'

class HistoricoMembroSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoMembro
        fields = '__all__'

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Informacoes
        fields = '__all__'