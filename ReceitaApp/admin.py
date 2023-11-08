from django.contrib import admin
from ReceitaApp.models import Categoria
from ReceitaApp.models import Receita


# Register your models here.

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'grau_de_dificuldade', 'categoria']

admin.site.register(Categoria)
admin.site.register(Receita)