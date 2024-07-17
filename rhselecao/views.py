from rest_framework import generics
from .models import Vagas, CandidaturaSimples
from .serializers import VagasSerializer, CadidaturaSerializer

#View Candidatura
class VagasListView(generics.ListCreateAPIView):
    queryset = Vagas.objects.all()
    serializer_class = VagasSerializer

class VagasRetrivieUpDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vagas.objects.all()
    serializer_class = VagasSerializer

#View Candidatura
class CandidaturaListView(generics.ListCreateAPIView):
    queryset = CandidaturaSimples.objects.all()
    serializer_class = CadidaturaSerializer

class CandidaturaRetrivieUpDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CandidaturaSimples.objects.all()
    serializer_class = CadidaturaSerializer
