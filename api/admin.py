from django.contrib import admin

from .models import Atendimento, Card, Ocupacao, Paciente, Preceptor, Resposta, Roteiro

@admin.register(Preceptor)
class PreceptorAdmin(admin.ModelAdmin):
    list_display = [
        
    ]
