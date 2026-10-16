from django.contrib import admin
from .models import Modalidade, Tecnico, Equipe, Atleta


class TecnicoInline(admin.StackedInline):
    model = Tecnico


class EquipeAdmin(admin.ModelAdmin):
    inlines = [TecnicoInline]


class AtletaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'matricula', 'equipe']
    list_filter = ['modalidades']
    search_fields = ['nome']


admin.site.register(Modalidade)
admin.site.register(Equipe, EquipeAdmin)
admin.site.register(Atleta, AtletaAdmin)
