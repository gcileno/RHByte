from typing import Any
from django.db import models


STATUS_VOLUNTARIO = (
    ('ATIVO','Ativo'),
    ('DESLIGADO', 'Desativado')
)

# Aqui vamos inserir os o modesl de configuração das empresa juniors
class Informacoes(models.Model):
    rua = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True, unique=True)

    def __str__(self):
        return f"Informacoes #{self.pk}"

class EmpresasJuinior(models.Model):
    razao_social = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=18)  # Use CharField para CNPJ
    inscricao_estadual = models.CharField(max_length=20)
    
    representante_legal = models.CharField(max_length=100)
    cpf_representante_lega = models.CharField(max_length=11)
    
    area_atuacao = models.CharField(max_length=100)
    site = models.URLField(blank=True)  
    fundacao = models.DateField()
    info_contato = models.ForeignKey(Informacoes, blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.razao_social}'

class Voluntario(models.Model):
    
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=20)
    status_civil = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    
    matricula_ies = models.CharField(max_length=20, unique=True)
    
    informacoes_voluntario = models.ForeignKey(
        Informacoes,
        on_delete=models.CASCADE, 
        null=True,blank=True,
        related_name="voluntarios")

    def __str__(self):
        return f'{self.nome}'

class Membro(models.Model):
    
    nome_voluntario = models.OneToOneField(
        "Voluntario",
        on_delete=models.DO_NOTHING,
        null=True, blank=True,
        related_name= "membros"
    )
    empresa_junior= models.ForeignKey(
        EmpresasJuinior, 
        on_delete=models.CASCADE, 
        null=True, blank=True,
        related_name="membros")
       
    nome_departamento = models.ForeignKey(
        "Departamento", 
        on_delete=models.CASCADE, 
        null=True, blank=True,
        related_name="membros")
    
    data_entrada = models.DateField(null=True, blank=True)
    data_saida = models.DateField(null=True, blank=True)
    
    periodo_entrada = models.CharField(max_length=50)
    periodo_saida = models.CharField(max_length=50, null=True, blank=True)

    status = models.CharField(max_length=9, choices= STATUS_VOLUNTARIO)


class Funcao(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class HistoricoMembro(models.Model):
   
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE, null=True, blank=True)
    
    historico_membro= models.ForeignKey(
        Membro, 
        on_delete=models.CASCADE, 
        null=True, blank=True,
        related_name="funcoes")
    
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    
    def __str__(self):
        if self.funcao:
            return self.funcao.nome
        return "Sem função definida"

class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    
    voluntario_lider = models.ForeignKey(
        Membro, 
        on_delete=models.SET_NULL,
        blank= True, 
        null=True, 
        related_name='lider_departamento')

    
    def __str__(self):
        return self.nome

