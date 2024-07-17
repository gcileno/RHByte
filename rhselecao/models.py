from django.db import models
from juniors.models import Funcao, Voluntario

STATUS_VAGA = (
        ('AB', 'Aberta'),
        ('FE', 'Fechada'),
        ('EP', 'Em Processo'),
        ('PA', 'Pausa'),
)

STATUS_CADIDATO = (
    ('--', 'Análise'),
    ('AP', 'Aprovado'),
    ('CR', 'Cadastro reserva'),
)

class Vagas(models.Model):
    
    nome = models.ForeignKey(Funcao, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(
        max_length=2,
        choices=STATUS_VAGA,
        default='FE',
    )
    
class CandidaturaSimples(models.Model):
    vaga = models.ForeignKey(
        Vagas,
        blank=True, null=True,
        on_delete=models.CASCADE, 
        related_name='candidaturas')
    
    candidato = models.ForeignKey(
        Voluntario,
        blank=True, null=True,
        on_delete=models.CASCADE,
        related_name='candidatos')
    
    status = models.CharField(
        max_length=2,
        choices=STATUS_CADIDATO,
        default='--',
    )

"""
Espaço para mais informações sobre a vaga seria interessate, como requisitos, perido que estara aberta
desevolver melhor a cadindatura para receber curriculos ou cadastrar curriculo do candidato.
"""