from django.contrib import admin
from SistemaEstoque import models
# Register your models here.
@admin.register(models.Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display=('id','nome','quantidade','preco','categoria',) # define quais colunas aparecem
    ordering= '-id',# ordena em ordem decresente pelo id
    list_per_page=40 # numeros de registros exebidos por pagina
    list_max_show_all=100 #numeros maximo de registros exebidos por pagina

#Para exibir no admin do django
@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display='nome',
    ordering='-id',