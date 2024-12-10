from django.urls import path
from .views import (
    JuniorsListView, JuniorsRetrivieUpDelView,
    VoluntarioListView, VoluntarioRetrivieUpDelView, VoluntarioCreateView,
    InformacaoListCreateView, InformacaoRetriveUpDetail,
    MembroListView, MembroRetrieveUpdateDestroyView,
    FuncaoListView, FuncaoRetrieveUpdateDestroyView,
    HistoricoMembroListView, HistoricoMembroRetrieveUpdateDestroyView,
    DepartamentoListView, DepartamentoRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('juniors/', JuniorsListView.as_view(), name='juniors-list'),
    path('juniors/<int:pk>/', JuniorsRetrivieUpDelView.as_view(), name='juniors-detail'),
    
    path('voluntario/cadastro/', VoluntarioCreateView.as_view(), name='cadastro-voluntario'),
    path('voluntarios/', VoluntarioListView.as_view(), name='voluntario-list'),
    path('voluntarios/<int:pk>/', VoluntarioRetrivieUpDelView.as_view(), name='voluntario-detail'),

    path("informacao/", InformacaoListCreateView.as_view(), name="informcoes-list"),
    path('informacao/<int:pk>/', InformacaoRetriveUpDetail.as_view(), name="info-detail"),
    
    path('membros/', MembroListView.as_view(), name='associados-list'),
    path('membro/<int:pk>/', MembroRetrieveUpdateDestroyView.as_view(), name='associados-detail'),
    
    path('funcoes/', FuncaoListView.as_view(), name='funcao-list'),
    path('funcoes/<int:pk>/', FuncaoRetrieveUpdateDestroyView.as_view(), name='funcao-detail'),
    
    path('historico/', HistoricoMembroListView.as_view(), name='cargo-list'),
    path('historico/<int:pk>/', HistoricoMembroRetrieveUpdateDestroyView.as_view(), name='cargo-detail'),
    
    path('departamentos/', DepartamentoListView.as_view(), name='departamento-list'),
    path('departamentos/<int:pk>/', DepartamentoRetrieveUpdateDestroyView.as_view(), name='departamento-detail'),
]