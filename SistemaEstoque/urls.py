from django.urls import path
from SistemaEstoque import views

app_name='SistemaEstoque'


urlpatterns = [
    path('', views.home, name='home'),
    path('novo_item/', views.add_item, name='novo_item'),
    path('nova_categoria/', views.add_ctg, name='nova_categoria'),
    path('inventario/', views.inventario , name='inventario'),
    path('inventario/search/', views.search , name='search'),
    path('update/<int:id_item>/', views.update , name='update'),
    path('<int:id_item>/', views.item_sozinho , name='item_sozinho'),
    path('delete/<int:id_item>/', views.delete , name='delete'),
    path('criar_usuario/',views.criar_user, name='criar_usuario'),
    path('atualizar_usuario/',views.atualizar_user, name='atualizar_usuario'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout, name='logout'),
]