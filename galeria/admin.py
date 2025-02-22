from django.contrib import admin

from galeria.models import Fotografia
# Register your models here.


class ListandoFotografias(admin.ModelAdmin):
    # add titulo as colunas nas listas de objetos cadastraddos no django-admin
    list_display = ('id', 'nome', 'legenda', 'publicada')
    # tornando toda a linha da lista como LINK, ao clicar em qualquer campo, ira para a tela de edicao
    list_display_links = ('id', 'nome', 'legenda')
    # add campo de busca por nome
    search_fields = ('nome',)
    # add campo de filtro por categoria
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    # add paginacao
    list_per_page = 10


admin.site.register(Fotografia, ListandoFotografias)
