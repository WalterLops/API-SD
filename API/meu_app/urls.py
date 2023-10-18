from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_dispositivo/', views.CadastroDispositivoList.as_view(), name='cadastro-dispositivo-list'),
    path('cadastro_dispositivo/<int:pk>/', views.CadastroDispositivoDetail.as_view(), name='cadastro-dispositivo-detail'),
    path('falha/', views.FalhaList.as_view(), name='falha-list'),
    path('falha/<int:pk>/', views.FalhaDetail.as_view(), name='falha-detail'),
    path('endpoints/', views.endpoint_list, name='endpoint-list'),
]
