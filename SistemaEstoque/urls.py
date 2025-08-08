from django.urls import path
from SistemaEstoque import views

app_name='SistemaEstoque'


urlpatterns = [
    path('', views.home, name='home'),
    path('inventario/', views.inventario, name='inventario'),
    path('novo_item/', views.add_item, name='novo_item'),
    path('nova_categoria/', views.add_ctg, name='nova_categoria'),
    path('inventario/', views.inventario , name='inventario'),
    path('inventario/search/', views.search , name='search'),
]