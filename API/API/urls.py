"""
URL configuration for API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from meu_app import views
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Minha API",
        default_version='v1',
        description="Descrição da minha API",
        terms_of_service="https://www.minhaapi.com/terms/",
        contact=openapi.Contact(email="contato@minhaapi.com"),
        license=openapi.License(name="Licença da API"),
    ),
    public=True,
    permission_classes=(AllowAny,),  # Define as permissões para a documentação
    authentication_classes=(JWTAuthentication,),  # Define a autenticação JWT
)


urlpatterns = [
   path('', views.escolher_documentacao, name='escolher-documentacao'),
   path('accounts/login/', TokenObtainPairView.as_view(), name='login'),
   path('accounts/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('accounts/token/refresh/', views.CustomTokenRefreshView.as_view(), name='token_refresh'),
   path('accounts/user/create/', views.CreateUserView.as_view(), name='user-create'),
   path('admin/', admin.site.urls),
   path('api/', include('meu_app.urls')),  
   #path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
   
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

from django.urls import path
