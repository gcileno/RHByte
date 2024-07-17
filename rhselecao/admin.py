from django.contrib import admin
from .models import Vagas, CandidaturaSimples

class VagasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'status',)
    search_fields = ('nome', 'status',)

class CadidaturasAdmin(admin.ModelAdmin):
    list_display= ('vaga',)
    search_fields = ('vaga',)

admin.site.register(Vagas,VagasAdmin)
admin.site.register(CandidaturaSimples, CadidaturasAdmin)


# Register your models here.
