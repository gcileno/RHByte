from django.contrib import admin
from .models import EmpresasJuinior, Membro, HistoricoMembro, Funcao, Departamento, Voluntario, Informacoes


class EmpresasJuiniorsAdmin(admin.ModelAdmin):
    list_display=('razao_social',)
    search_fields = ('razao_social','cnpj',)

class AssociadosAdmin(admin.ModelAdmin):
    list_display=('nome_voluntario',)
    search_fields = ('nome_voluntario', 'status',)

class VoluntarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula_ies',)
    search_fields = ('nome', 'matricula_ies', 'cpf',)
    
class FuncaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)

class HistoricoMembroAdmin(admin.ModelAdmin):
    list_display=('funcao', 'historico_membro',)
    search_fields = ('funcao',)

class DepartamentoAdmin(admin.ModelAdmin):
    list_display=('nome',)
    search_fields = ('nome',)
    
admin.site.register(EmpresasJuinior, EmpresasJuiniorsAdmin)
admin.site.register(Membro, AssociadosAdmin)
admin.site.register(Funcao, FuncaoAdmin)
admin.site.register(HistoricoMembro, HistoricoMembroAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Voluntario, VoluntarioAdmin)
admin.site.register(Informacoes)
