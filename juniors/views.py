from rest_framework import generics
from .models import EmpresasJuinior, Voluntario
from .serializers import *

class JuniorsListView(generics.ListCreateAPIView):
    queryset = EmpresasJuinior.objects.all()
    serializer_class = JuniorSerializer

class JuniorsRetrivieUpDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmpresasJuinior.objects.all()
    serializer_class = JuniorSerializer

class VoluntarioCreateView(generics.CreateAPIView):
    serializer_class = VoluntarioSerializer

class VoluntarioListView(generics.ListCreateAPIView):
    queryset = Voluntario.objects.all()
    serializer_class = VoluntarioSerializer

class VoluntarioRetrivieUpDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Voluntario.objects.all()
    serializer_class = VoluntarioSerializer

class InforCreateView(generics.CreateAPIView):
    serializer_class = VoluntarioSerializer

class InformacaoListCreateView(generics.ListCreateAPIView):
    queryset = Informacoes.objects.all()
    serializer_class = InformationSerializer

class InformacaoRetriveUpDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Informacoes.objects.all()
    serializer_class = InformationSerializer

# Views para Membro
class MembroListView(generics.ListCreateAPIView):
    queryset = Membro.objects.all()
    serializer_class = MembroSerializer

class MembroRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Membro.objects.all()
    serializer_class = MembroSerializer

# Views para Funcao
class FuncaoListView(generics.ListCreateAPIView):
    queryset = Funcao.objects.all()
    serializer_class = FuncaoSerializer

class FuncaoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Funcao.objects.all()
    serializer_class = FuncaoSerializer

# Views para HistoricoMembro
class HistoricoMembroListView(generics.ListCreateAPIView):
    queryset = HistoricoMembro.objects.all()
    serializer_class = HistoricoMembroSerializer

class HistoricoMembroRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistoricoMembro.objects.all()
    serializer_class = HistoricoMembroSerializer

# Views para Departamento
class DepartamentoListView(generics.ListCreateAPIView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class DepartamentoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
