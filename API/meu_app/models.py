from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission, Group
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    # Adicione o related_name para evitar conflitos
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')

    def __str__(self):
        return self.username

class CadastroDispositivo(models.Model):
    departamento = models.CharField(max_length=100)
    laboratorio = models.CharField(max_length=100)
    dispositivo = models.CharField(max_length=100)
    identificacao_dispositivo = models.CharField(max_length=50)
    especificacoes_tecnicas = models.TextField()
    data_aquisicao = models.DateField()

    def __str__(self):  
        return f'{self.departamento} - {self.laboratorio} - {self.dispositivo}'
    

class Falha(models.Model):
    departamento = models.CharField(max_length=100)
    laboratorio = models.CharField(max_length=100)
    tipo_manutencao = models.CharField(max_length=50)
    dispositivo = models.ForeignKey('CadastroDispositivo', on_delete=models.CASCADE)
    identificacao_dispositivo = models.CharField(max_length=50)
    descricao_falha = models.TextField()
    data_ocorrencia = models.DateField()

    def _str_(self):
        return f'Falha em {self.dispositivo.nome} - {self.data_ocorrencia}'
