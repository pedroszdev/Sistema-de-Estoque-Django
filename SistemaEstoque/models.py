from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Categoria(models.Model):
    nome=models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome


class Estoque(models.Model):
    nome=models.CharField(max_length=50,)
    quantidade=models.IntegerField(max_length=50, default=0)
    preco=models.FloatField(default=0)
    data_criacao=models.DateTimeField(default=timezone.now)
    categoria=models.ForeignKey(Categoria,on_delete=models.SET_NULL,blank=True,null=True)
    criador=models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    
    def __str__(self):
        return f'{self.nome}'