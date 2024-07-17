from django.urls import path
from . import views

urlpatterns = [
    path('vagas/', views.VagasListView.as_view(), name='vagas-list-criar'),
    path('vagas/<int:id>/', views.VagasRetrivieUpDelView.as_view(), name='vaga-retriv'),
    
    path('candidatura/', views.CandidaturaListView.as_view(), name='candidatura-list-criar'),
    path('candidatura/<int:id>/', views.CandidaturaRetrivieUpDelView.as_view(),name='candidatura-retriv')
]